# Settings
# --------

UNAME_S := $(shell uname -s)

DEPS_DIR      := deps
BUILD_DIR     := .build
NODE_DIR      := $(abspath node)
BUILD_LOCAL   := $(abspath $(BUILD_DIR)/local)
LOCAL_LIB     := $(BUILD_LOCAL)/lib
LOCAL_BIN     := $(BUILD_LOCAL)/bin
export NODE_DIR
export LOCAL_LIB

INSTALL_PREFIX  := /usr
INSTALL_BIN     ?= $(INSTALL_PREFIX)/bin
INSTALL_LIB     ?= $(INSTALL_PREFIX)/lib/kevm
INSTALL_INCLUDE ?= $(INSTALL_LIB)/include

KEVM_BIN     := $(BUILD_DIR)$(INSTALL_BIN)
KEVM_LIB     := $(BUILD_DIR)$(INSTALL_LIB)
KEVM_INCLUDE := $(KEVM_LIB)/include
KEVM_K_BIN   := $(KEVM_LIB)/kframework/bin
KEVM         := kevm
KEVM_LIB_ABS := $(abspath $(KEVM_LIB))
export KEVM_LIB_ABS

KEVM_VERSION     ?= $(shell cat package/version)
KEVM_RELEASE_TAG ?= v$(KEVM_VERSION)-$(shell git rev-parse --short HEAD)

K_SUBMODULE := $(DEPS_DIR)/k

LIBRARY_PATH       := $(LOCAL_LIB):$(KEVM_LIB_ABS)/libff/lib
C_INCLUDE_PATH     += :$(BUILD_LOCAL)/include
CPLUS_INCLUDE_PATH += :$(BUILD_LOCAL)/include
PATH               := $(abspath $(KEVM_BIN)):$(abspath $(KEVM_K_BIN)):$(LOCAL_BIN):$(PATH)

export LIBRARY_PATH
export C_INCLUDE_PATH
export CPLUS_INCLUDE_PATH
export PATH

PLUGIN_SUBMODULE := $(DEPS_DIR)/plugin
PLUGIN_SOURCE    := $(KEVM_INCLUDE)/kframework/blockchain-k-plugin/krypto.md
PLUGIN_FULL_PATH := $(abspath ${PLUGIN_SUBMODULE})
export PLUGIN_FULL_PATH


.PHONY: all clean distclean                                                                                                                  \
        deps k-deps plugin-deps libsecp256k1 libff protobuf                                                                                  \
        build build-haskell build-haskell-standalone build-foundry build-llvm build-prove build-prove-haskell build-node build-kevm          \
        test test-all test-conformance test-rest-conformance test-all-conformance test-slow-conformance test-failing-conformance             \
        test-vm test-rest-vm test-all-vm test-bchain test-rest-bchain test-all-bchain test-node                                              \
        test-prove test-failing-prove test-foundry-kcfg-diff                                                                                 \
        test-prove-benchmarks test-prove-functional test-prove-opcodes test-prove-erc20 test-prove-bihu test-prove-examples test-prove-smoke \
        test-prove-mcd test-klab-prove                                                                                                       \
        test-parse test-failure test-foundry-kompile test-foundry-prove test-foundry-bmc-prove test-foundry-list                             \
        test-interactive test-interactive-help test-interactive-run test-interactive-prove test-interactive-search                           \
        test-kevm-pyk foundry-forge-build foundry-forge-test foundry-clean foundry-fail                                                      \
        media media-pdf metropolis-theme                                                                                                     \
        install uninstall                                                                                                                    \
        poetry-env poetry shell kevm-pyk
.SECONDARY:

all: build

clean: foundry-clean
	rm -rf $(KEVM_BIN) $(KEVM_LIB)

distclean:
	rm -rf $(BUILD_DIR)

# Non-K Dependencies
# ------------------

libsecp256k1_out := $(LOCAL_LIB)/pkgconfig/libsecp256k1.pc
libff_out        := $(KEVM_LIB)/libff/lib/libff.a
libcryptopp_out  := $(KEVM_LIB)/cryptopp/lib/libcryptopp.a
protobuf_out     := $(LOCAL_LIB)/proto/proto/msg.pb.cc

libsecp256k1: $(libsecp256k1_out)
libff:        $(libff_out)
libcryptopp : $(libcryptopp_out)
protobuf:     $(protobuf_out)

$(libsecp256k1_out): $(PLUGIN_SUBMODULE)/deps/secp256k1/autogen.sh
	cd $(PLUGIN_SUBMODULE)/deps/secp256k1                                 \
	    && ./autogen.sh                                                   \
	    && ./configure --enable-module-recovery --prefix="$(BUILD_LOCAL)" \
	    && $(MAKE)                                                        \
	    && $(MAKE) install

LIBFF_CMAKE_FLAGS :=

ifeq ($(UNAME_S),Linux)
    LIBFF_CMAKE_FLAGS +=
else ifeq ($(UNAME_S),Darwin)
    LIBFF_CMAKE_FLAGS += -DWITH_PROCPS=OFF -DOPENSSL_ROOT_DIR=$(shell brew --prefix openssl)
else
    LIBFF_CMAKE_FLAGS += -DWITH_PROCPS=OFF
endif

ifneq ($(APPLE_SILICON),)
    LIBFF_CMAKE_FLAGS += -DCURVE=ALT_BN128 -DUSE_ASM=Off
endif

ifeq ($(LIBFF_NO_FPIC),)
    LIBFF_CMAKE_FLAGS += -DCMAKE_CXX_FLAGS=-fPIC
endif

$(libff_out): $(PLUGIN_SUBMODULE)/deps/libff/CMakeLists.txt
	@mkdir -p $(PLUGIN_SUBMODULE)/deps/libff/build
	cd $(PLUGIN_SUBMODULE)/deps/libff/build                                                                     \
	    && cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$(INSTALL_LIB)/libff $(LIBFF_CMAKE_FLAGS) \
	    && make -s -j4                                                                                          \
	    && make install DESTDIR=$(CURDIR)/$(BUILD_DIR)

$(protobuf_out): $(NODE_DIR)/proto/msg.proto
	@mkdir -p $(LOCAL_LIB)/proto
	protoc --cpp_out=$(LOCAL_LIB)/proto -I $(NODE_DIR) $(NODE_DIR)/proto/msg.proto

$(libcryptopp_out): $(PLUGIN_SUBMODULE)/deps/cryptopp/GNUmakefile
	cd $(PLUGIN_SUBMODULE)/deps/cryptopp                            \
            && $(MAKE) install DESTDIR=$(CURDIR)/$(BUILD_DIR) PREFIX=$(INSTALL_LIB)/cryptopp

# K Dependencies
# --------------

deps: k-deps

K_MVN_ARGS :=
ifneq ($(SKIP_LLVM),)
    K_MVN_ARGS += -Dllvm.backend.skip
endif
ifneq ($(SKIP_HASKELL),)
    K_MVN_ARGS += -Dhaskell.backend.skip
endif

ifneq ($(APPLE_SILICON),)
    K_MVN_ARGS += -Dstack.extra-opts='--compiler ghc-8.10.7 --system-ghc'
endif

ifneq ($(RELEASE),)
    K_BUILD_TYPE := FastBuild
else
    K_BUILD_TYPE := Debug
endif

k-deps:
	cd $(K_SUBMODULE)                                                                                                                                                                            \
	    && mvn --batch-mode package -DskipTests -Dllvm.backend.prefix=$(INSTALL_LIB)/kframework -Dllvm.backend.destdir=$(CURDIR)/$(BUILD_DIR) -Dproject.build.type=$(K_BUILD_TYPE) $(K_MVN_ARGS) \
	    && DESTDIR=$(CURDIR)/$(BUILD_DIR) PREFIX=$(INSTALL_LIB)/kframework package/package

plugin_k_include  := $(KEVM_INCLUDE)/kframework/plugin
plugin_include    := $(KEVM_LIB)/blockchain-k-plugin/include
plugin_k          := krypto.md
plugin_c          := plugin_util.cpp crypto.cpp blake2.cpp plugin_util.h blake2.h
plugin_includes   := $(patsubst %, $(plugin_k_include)/%, $(plugin_k))
plugin_c_includes := $(patsubst %, $(plugin_include)/c/%, $(plugin_c))

$(plugin_include)/c/%: $(PLUGIN_SUBMODULE)/plugin-c/%
	@mkdir -p $(dir $@)
	install $< $@

$(plugin_k_include)/%: $(PLUGIN_SUBMODULE)/plugin/%
	@mkdir -p $(dir $@)
	install $< $@

plugin-deps: $(plugin_includes) $(plugin_c_includes)


# Building
# --------

PYTHON_BIN   := python3.10
KEVM_PYK_DIR := ./kevm-pyk
POETRY       := poetry -C $(KEVM_PYK_DIR)
POETRY_RUN   := $(POETRY) run --

poetry-env:
	$(POETRY) env use $(PYTHON_BIN)

poetry: poetry-env
	$(POETRY) install

shell: poetry
	$(POETRY) shell

kevm-pyk: poetry-env
	$(MAKE) -C $(KEVM_PYK_DIR)

kevm_files := abi.md                          \
              asm.md                          \
              buf.md                          \
              data.md                         \
              driver.md                       \
              edsl.md                         \
              evm.md                          \
              evm-types.md                    \
              evm-node.md                     \
              foundry.md                      \
              hashed-locations.md             \
              gas.md                          \
              infinite-gas.md                 \
              json-rpc.md                     \
              network.md                      \
              optimizations.md                \
              serialization.md                \
              state-utils.md                  \
              word.md                         \
              lemmas/lemmas.k                 \
              lemmas/evm-int-simplification.k \
              lemmas/int-simplification.k     \
              lemmas/bitwise-simplification.k \
              lemmas/bytes-simplification.k

kevm_includes := $(patsubst %, $(KEVM_INCLUDE)/kframework/%, $(kevm_files))

includes := $(kevm_includes) $(plugin_includes) $(plugin_c_includes)

$(KEVM_INCLUDE)/%: include/%
	@mkdir -p $(dir $@)
	install $< $@

$(KEVM_INCLUDE)/kframework/lemmas/%.k: tests/specs/%.k
	@mkdir -p $(dir $@)
	install $< $@

KEVM_PYK              := $(POETRY_RUN) kevm-pyk
KOMPILE               := KEVM_LIB=$(KEVM_LIB) $(KEVM_PYK) kompile
KOMPILE_MAIN_FILE     :=
KOMPILE_TARGET        :=
KOMPILE_MAIN_MODULE   :=
KOMPILE_SYNTAX_MODULE :=

KOMPILE_OPTS :=
ifneq (,$(RELEASE))
    KOMPILE_OPTS += -O2
endif

kompile =                                        \
    $(KOMPILE)                                   \
        $(KOMPILE_MAIN_FILE)                     \
        --target $(KOMPILE_TARGET)               \
        --main-module $(KOMPILE_MAIN_MODULE)     \
        --syntax-module $(KOMPILE_SYNTAX_MODULE) \
        $(KOMPILE_OPTS)


# Haskell

haskell_dir      := haskell
haskell_kompiled := $(haskell_dir)/definition.kore
kompile_haskell  := $(KEVM_LIB)/$(haskell_kompiled)

ifeq ($(UNAME_S),Darwin)
$(kompile_haskell): $(libsecp256k1_out)
endif

$(kompile_haskell): $(kevm_includes) $(plugin_includes)

$(kompile_haskell): KOMPILE_TARGET        := haskell
$(kompile_haskell): KOMPILE_MAIN_FILE     := $(KEVM_INCLUDE)/kframework/edsl.md
$(kompile_haskell): KOMPILE_MAIN_MODULE   := EDSL
$(kompile_haskell): KOMPILE_SYNTAX_MODULE := EDSL
$(kompile_haskell):
	$(kompile)


# Standalone

llvm_dir      := llvm
llvm_kompiled := $(llvm_dir)/interpreter
kompile_llvm  := $(KEVM_LIB)/$(llvm_kompiled)

ifeq ($(UNAME_S),Darwin)
$(kompile_llvm): $(libcryptopp_out)
endif

$(kompile_llvm): $(kevm_includes) $(plugin_includes) $(plugin_c_includes) $(libff_out)

$(kompile_llvm): KOMPILE_TARGET        := llvm
$(kompile_llvm): KOMPILE_MAIN_FILE     := $(KEVM_INCLUDE)/kframework/driver.md
$(kompile_llvm): KOMPILE_MAIN_MODULE   := ETHEREUM-SIMULATION
$(kompile_llvm): KOMPILE_SYNTAX_MODULE := ETHEREUM-SIMULATION
$(kompile_llvm):
	$(kompile)


# Haskell Standalone

haskell_standalone_dir      := haskell-standalone
haskell_standalone_kompiled := $(haskell_standalone_dir)/definition.kore
kompile_haskell_standalone  := $(KEVM_LIB)/$(haskell_standalone_kompiled)

ifeq ($(UNAME_S),Darwin)
$(kompile_haskell_standalone): $(libsecp256k1_out)
endif

$(kompile_haskell_standalone): $(kevm_includes) $(plugin_includes)

$(kompile_haskell_standalone): KOMPILE_TARGET        := haskell-standalone
$(kompile_haskell_standalone): KOMPILE_MAIN_FILE     := $(KEVM_INCLUDE)/kframework/driver.md
$(kompile_haskell_standalone): KOMPILE_MAIN_MODULE   := ETHEREUM-SIMULATION
$(kompile_haskell_standalone): KOMPILE_SYNTAX_MODULE := ETHEREUM-SIMULATION
$(kompile_haskell_standalone):
	$(kompile)


# Node
#
node_dir      := node
node_kore     := $(node_dir)/definition.kore
node_kompiled := $(node_dir)/build/kevm-vm
kompile_node  := $(KEVM_LIB)/$(node_kore)
export node_dir

$(kompile_node): $(kevm_includes) $(plugin_includes) $(plugin_c_includes) $(libff_out)

$(kompile_node): KOMPILE_TARGET        := node
$(kompile_node): KOMPILE_MAIN_FILE     := $(KEVM_INCLUDE)/kframework/evm-node.md
$(kompile_node): KOMPILE_MAIN_MODULE   := EVM-NODE
$(kompile_node): KOMPILE_SYNTAX_MODULE := EVM-NODE
$(kompile_node):
	$(kompile)


$(KEVM_LIB)/$(node_kompiled): $(KEVM_LIB)/$(node_kore) $(protobuf_out) $(libff_out)
	@mkdir -p $(dir $@)
	cd $(dir $@) && cmake $(CURDIR)/cmake/node -DCMAKE_INSTALL_PREFIX=$(INSTALL_LIB)/$(node_dir) && $(MAKE)


# Foundry

foundry_dir      := foundry
foundry_kompiled := $(foundry_dir)/definition.kore
kompile_foundry  := $(KEVM_LIB)/$(foundry_kompiled)

ifeq ($(UNAME_S),Darwin)
$(kompile_foundry): $(libsecp256k1_out)
endif

$(kompile_foundry): $(kevm_includes) $(plugin_includes) $(lemma_includes)

$(kompile_foundry): KOMPILE_TARGET        := foundry
$(kompile_foundry): KOMPILE_MAIN_FILE     := $(KEVM_INCLUDE)/kframework/foundry.md
$(kompile_foundry): KOMPILE_MAIN_MODULE   := FOUNDRY
$(kompile_foundry): KOMPILE_SYNTAX_MODULE := FOUNDRY
$(kompile_foundry):
	$(kompile)


# Installing
# ----------

install_bins := kevm    \
                kevm-vm

install_libs := $(haskell_kompiled)                                        \
                $(llvm_kompiled)                                           \
                $(foundry_kompiled)                                        \
                $(haskell_standalone_kompiled)                             \
                $(patsubst %, include/kframework/lemmas/%, $(kevm_lemmas)) \
                kore-json.py                                               \
                release.md                                                 \
                version

$(KEVM_BIN)/%: bin/%
	@mkdir -p $(dir $@)
	install $< $@

$(KEVM_BIN)/kevm-vm: $(KEVM_LIB)/$(node_kompiled)
	@mkdir -p $(dir $@)
	install $< $@

$(KEVM_LIB)/%.py: scripts/%.py
	@mkdir -p $(dir $@)
	install $< $@

$(KEVM_LIB)/version: package/version
	@mkdir -p $(dir $@)
	install $< $@

$(KEVM_LIB)/release.md: INSTALL.md
	@mkdir -p $(dir $@)
	echo "KEVM Release $(shell cat package/version)"  > $@
	echo                                             >> $@
	cat INSTALL.md                                   >> $@

build: $(patsubst %, $(KEVM_BIN)/%, $(install_bins)) $(patsubst %, $(KEVM_LIB)/%, $(install_libs))

build-llvm:               $(KEVM_LIB)/$(llvm_kompiled)    $(KEVM_LIB)/kore-json.py
build-haskell:            $(KEVM_LIB)/$(haskell_kompiled) $(KEVM_LIB)/kore-json.py
build-haskell-standalone: $(KEVM_LIB)/$(haskell_standalone_kompiled) $(KEVM_LIB)/kore-json.py
build-node:               $(KEVM_LIB)/$(node_kompiled)
build-kevm:               $(KEVM_BIN)/kevm $(KEVM_LIB)/version $(kevm_includes) $(plugin_includes)
build-foundry:            $(KEVM_BIN)/kevm $(KEVM_LIB)/$(foundry_kompiled) $(KEVM_LIB)/kore-json.py

all_bin_sources := $(shell find $(KEVM_BIN) -type f | sed 's|^$(KEVM_BIN)/||')
all_lib_sources := $(shell find $(KEVM_LIB) -type f                                            \
                            -not -path "$(KEVM_LIB)/**/dt/*"                                   \
                            -not -path "$(KEVM_LIB)/kframework/share/kframework/pl-tutorial/*" \
                            -not -path "$(KEVM_LIB)/kframework/share/kframework/k-tutorial/*"  \
                        | sed 's|^$(KEVM_LIB)/||')

install: $(patsubst %, $(DESTDIR)$(INSTALL_BIN)/%, $(all_bin_sources)) \
         $(patsubst %, $(DESTDIR)$(INSTALL_LIB)/%, $(all_lib_sources))

$(DESTDIR)$(INSTALL_BIN)/%: $(KEVM_BIN)/%
	@mkdir -p $(dir $@)
	install $< $@

$(DESTDIR)$(INSTALL_LIB)/%: $(KEVM_LIB)/%
	@mkdir -p $(dir $@)
	install $< $@

uninstall:
	rm -rf $(DESTDIR)$(INSTALL_BIN)/kevm
	rm -rf $(DESTDIR)$(INSTALL_LIB)/kevm

# Tests
# -----

TEST_CONCRETE_BACKEND := llvm
TEST_SYMBOLIC_BACKEND := haskell

CHECK := git --no-pager diff --no-index --ignore-all-space -R

KEVM_MODE     := NORMAL
KEVM_SCHEDULE := MERGE
KEVM_CHAINID  := 1

KPROVE_MODULE  = VERIFICATION
KPROVE_FILE    = verification
KPROVE_EXT     = k

KEVM_OPTS    ?=
KPROVE_OPTS  ?=
KAST_OPTS    ?=
KRUN_OPTS    ?=
KSEARCH_OPTS ?=

KEEP_OUTPUTS := false

test-all: test-all-conformance test-prove test-interactive test-parse test-kevm-pyk
test: test-conformance test-prove test-interactive test-parse test-kevm-pyk

# Generic Test Harnesses

tests/ethereum-tests/LegacyTests/Constantinople/VMTests/%: KEVM_MODE     = VMTESTS
tests/ethereum-tests/LegacyTests/Constantinople/VMTests/%: KEVM_SCHEDULE = DEFAULT

tests/specs/benchmarks/functional-spec%:              KPROVE_FILE   =  functional-spec
tests/specs/benchmarks/functional-spec%:              KPROVE_MODULE =  FUNCTIONAL-SPEC-SYNTAX
tests/specs/bihu/functional-spec%:                    KPROVE_FILE   =  functional-spec
tests/specs/bihu/functional-spec%:                    KPROVE_MODULE =  FUNCTIONAL-SPEC-SYNTAX
tests/specs/erc20/functional-spec%:                   KPROVE_MODULE =  FUNCTIONAL-SPEC-SYNTAX
tests/specs/examples/solidity-code-spec%:             KPROVE_EXT    =  md
tests/specs/examples/solidity-code-spec%:             KPROVE_FILE   =  solidity-code-spec
tests/specs/examples/erc20-spec%:                     KPROVE_EXT    =  md
tests/specs/examples/erc20-spec%:                     KPROVE_FILE   =  erc20-spec
tests/specs/examples/erc721-spec%:                    KPROVE_EXT    =  md
tests/specs/examples/erc721-spec%:                    KPROVE_FILE   =  erc721-spec
tests/specs/examples/storage-spec%:                   KPROVE_EXT    =  md
tests/specs/examples/storage-spec%:                   KPROVE_FILE   =  storage-spec
tests/specs/examples/sum-to-n-spec%:                  KPROVE_FILE   =  sum-to-n-spec
tests/specs/examples/sum-to-n-foundry-spec%:          KPROVE_FILE   =  sum-to-n-foundry-spec
tests/specs/functional/infinite-gas-spec%:            KPROVE_FILE   =  infinite-gas-spec
tests/specs/functional/evm-int-simplifications-spec%: KPROVE_FILE   =  evm-int-simplifications-spec
tests/specs/functional/int-simplifications-spec%:     KPROVE_FILE   =  int-simplifications-spec
tests/specs/functional/lemmas-no-smt-spec%:           KPROVE_FILE   =  lemmas-no-smt-spec
tests/specs/functional/lemmas-no-smt-spec%:           KPROVE_OPTS   += --haskell-backend-command "kore-exec --smt=none"
tests/specs/functional/lemmas-spec%:                  KPROVE_FILE   =  lemmas-spec
tests/specs/functional/merkle-spec%:                  KPROVE_FILE   =  merkle-spec
tests/specs/functional/storageRoot-spec%:             KPROVE_FILE   =  storageRoot-spec
tests/specs/mcd/functional-spec%:                     KPROVE_FILE   =  functional-spec
tests/specs/mcd/functional-spec%:                     KPROVE_MODULE =  FUNCTIONAL-SPEC-SYNTAX
tests/specs/opcodes/evm-optimizations-spec%:          KPROVE_EXT    =  md
tests/specs/opcodes/evm-optimizations-spec%:          KPROVE_FILE   =  evm-optimizations-spec
tests/specs/opcodes/evm-optimizations-spec%:          KPROVE_MODULE =  EVM-OPTIMIZATIONS-SPEC-LEMMAS

tests/%.run: tests/%
	$(KEVM) interpret $< $(KEVM_OPTS) $(KRUN_OPTS) --backend $(TEST_CONCRETE_BACKEND)                                  \
	    --mode $(KEVM_MODE) --schedule $(KEVM_SCHEDULE) --chainid $(KEVM_CHAINID)                                      \
	    > tests/$*.$(TEST_CONCRETE_BACKEND)-out                                                                        \
	    || $(CHECK) tests/$*.$(TEST_CONCRETE_BACKEND)-out tests/templates/output-success-$(TEST_CONCRETE_BACKEND).json
	$(KEEP_OUTPUTS) || rm -rf tests/$*.$(TEST_CONCRETE_BACKEND)-out

tests/%.run-interactive: tests/%
	$(KEVM) run $< $(KEVM_OPTS) $(KRUN_OPTS) --backend $(TEST_CONCRETE_BACKEND)                                        \
	    --mode $(KEVM_MODE) --schedule $(KEVM_SCHEDULE) --chainid $(KEVM_CHAINID)                                      \
	    > tests/$*.$(TEST_CONCRETE_BACKEND)-out                                                                        \
	    || $(CHECK) tests/$*.$(TEST_CONCRETE_BACKEND)-out tests/templates/output-success-$(TEST_CONCRETE_BACKEND).json
	$(KEEP_OUTPUTS) || rm -rf tests/$*.$(TEST_CONCRETE_BACKEND)-out

tests/%.run-expected: tests/% tests/%.expected
	$(KEVM) run $< $(KEVM_OPTS) $(KRUN_OPTS) --backend $(TEST_CONCRETE_BACKEND)    \
	    --mode $(KEVM_MODE) --schedule $(KEVM_SCHEDULE) --chainid $(KEVM_CHAINID)  \
	    > tests/$*.$(TEST_CONCRETE_BACKEND)-out                                    \
	    || $(CHECK) tests/$*.$(TEST_CONCRETE_BACKEND)-out tests/$*.expected
	$(KEEP_OUTPUTS) || rm -rf tests/$*.$(TEST_CONCRETE_BACKEND)-out

tests/%.parse: tests/% $(KEVM_LIB)/kore-json.py
	$(KEVM) kast $< $(KEVM_OPTS) $(KAST_OPTS) --backend $(TEST_CONCRETE_BACKEND) > $@-out
	$(CHECK) $@-out $@-expected
	$(KEEP_OUTPUTS) || rm -rf $@-out

tests/interactive/%.json.gst-to-kore.check: tests/ethereum-tests/GeneralStateTests/VMTests/%.json $(KEVM_BIN)/kevm
	$(KEVM) kast $< $(KEVM_OPTS) $(KAST_OPTS) > tests/interactive/$*.gst-to-kore.out
	$(CHECK) tests/interactive/$*.gst-to-kore.out tests/interactive/$*.gst-to-kore.expected
	$(KEEP_OUTPUTS) || rm -rf tests/interactive/$*.gst-to-kore.out

# solc-to-k
# ---------

FOUNDRY_PAR := 4

foundry-clean:
	rm -rf tests/foundry/cache
	rm -rf tests/foundry/out
	rm -f  tests/foundry/foundry.debug-log
	rm -f  tests/foundry/foundry.k
	rm -f  tests/foundry/foundry.rule-profile

tests/foundry/%: KEVM := $(POETRY_RUN) kevm

foundry_dir := tests/foundry
foundry_out := $(foundry_dir)/out

test-foundry-%: KEVM_OPTS += --pyk --verbose
test-foundry-%: KEVM := $(POETRY_RUN) kevm
test-foundry-kompile: tests/foundry/foundry.k.check tests/foundry/contracts.k.check
test-foundry-prove: tests/foundry/out/kompiled/foundry.k.prove
test-foundry-bmc-prove: tests/foundry/out/kompiled/foundry.k.bmc-prove
test-foundry-list: tests/foundry/foundry-list.check

foundry-forge-build: $(foundry_out)

foundry-forge-test: foundry-forge-build
	cd $(foundry_dir) && forge test --ffi

$(foundry_out):
	rm -rf $@
	cd $(dir $@) && forge build

tests/foundry/foundry-list.out: tests/foundry/out/kompiled/foundry.k.prove foundry-fail
	$(KEVM) foundry-list --foundry-project-root $(foundry_dir) > $@

tests/foundry/foundry-list.check: tests/foundry/foundry-list.out
	grep --invert-match 'path:' $< > $@.stripped
	$(CHECK) $@.stripped $@.expected

tests/foundry/foundry.k.check: tests/foundry/out/kompiled/foundry.k
	grep --invert-match '    rule  ( #binRuntime (' $< > $@.stripped
	$(CHECK) $@.stripped $@.expected

tests/foundry/contracts.k.check: tests/foundry/out/kompiled/contracts.k
	grep --invert-match '    rule  ( #binRuntime (' $< > $@.stripped
	$(CHECK) $@.stripped $@.expected

tests/foundry/out/kompiled/foundry.k: tests/foundry/out/kompiled/timestamp
tests/foundry/out/kompiled/contracts.k: tests/foundry/out/kompiled/timestamp

tests/foundry/out/kompiled/foundry.k.prove: tests/foundry/out/kompiled/timestamp
	$(KEVM) foundry-prove --foundry-project-root $(foundry_dir)          \
	    -j$(FOUNDRY_PAR) --no-simplify-init --max-depth 1000             \
	    $(KEVM_OPTS) $(KPROVE_OPTS)                                      \
	    $(addprefix --exclude-test , $(shell cat tests/foundry/exclude))

tests/foundry/out/kompiled/foundry.k.bmc-prove: tests/foundry/out/kompiled/timestamp
	$(KEVM) foundry-prove --foundry-project-root $(foundry_dir)          \
	    -j$(FOUNDRY_PAR) --no-simplify-init --max-depth 1000             \
            --bmc-depth 3                                                    \
	    $(KEVM_OPTS) $(KPROVE_OPTS)                                      \
	    $(addprefix --test , $(shell cat tests/foundry/bmc-tests))

foundry_golden := tests/foundry/golden
foundry_diff_tests := $(shell cat tests/foundry/checkoutput)

test-foundry-kcfg-diff: $(patsubst %, $(foundry_golden)/%.check, $(foundry_diff_tests))

foundry-fail: tests/foundry/out/kompiled/timestamp
	$(KEVM) foundry-prove                                \
	--foundry-project-root $(foundry_dir)                \
	-j$(FOUNDRY_PAR) --no-simplify-init --max-depth 1000 \
	$(KEVM_OPTS) $(KPROVE_OPTS)                          \
	$(addprefix --test , $(foundry_diff_tests)) || true

foundry_show_opts := --to-module --omit-unstable-output --frontier --stuck

$(foundry_golden)/%.check: $(foundry_golden)/%.out
	$(CHECK) $(foundry_golden)/$*.out $(foundry_golden)/$*.expected

$(foundry_golden)/%.out: foundry-fail
	$(KEVM) foundry-show $(foundry_show_opts)                   \
	--foundry-project-root $(foundry_dir) $*                    \
	| grep --invert-match 'rule \[BASIC-BLOCK-'                 \
	| grep --invert-match '\[priority(.*), label(BASIC-BLOCK-'  \
	> $@

tests/foundry/out/kompiled/timestamp: $(foundry_out) $(KEVM_LIB)/$(foundry_kompiled) $(lemma_includes) poetry
	$(KEVM) foundry-kompile --foundry-project-root $(foundry_dir) $(KEVM_OPTS) --verbose --require $(foundry_dir)/lemmas.k --module-import LoopsTest:SUM-TO-N-INVARIANT

tests/specs/examples/%-bin-runtime.k: KEVM_OPTS += --pyk --verbose
tests/specs/examples/%-bin-runtime.k: KEVM := $(POETRY_RUN) kevm

tests/specs/examples/erc20-spec/haskell/timestamp: tests/specs/examples/erc20-bin-runtime.k
tests/specs/examples/erc20-bin-runtime.k: tests/specs/examples/ERC20.sol $(KEVM_LIB)/$(haskell_kompiled) poetry
	$(KEVM) solc-to-k $< ERC20 $(KEVM_OPTS) --verbose --definition $(KEVM_LIB)/$(haskell_dir) --main-module ERC20-VERIFICATION > $@

tests/specs/examples/erc721-spec/haskell/timestamp: tests/specs/examples/erc721-bin-runtime.k
tests/specs/examples/erc721-bin-runtime.k: tests/specs/examples/ERC721.sol $(KEVM_LIB)/$(haskell_kompiled) poetry
	$(KEVM) solc-to-k $< ERC721 $(KEVM_OPTS) --verbose --definition $(KEVM_LIB)/$(haskell_dir) --main-module ERC721-VERIFICATION > $@

tests/specs/examples/storage-spec/haskell/timestamp: tests/specs/examples/storage-bin-runtime.k
tests/specs/examples/storage-bin-runtime.k: tests/specs/examples/Storage.sol $(KEVM_LIB)/$(haskell_kompiled) poetry
	$(KEVM) solc-to-k $< Storage $(KEVM_OPTS) --verbose --definition $(KEVM_LIB)/$(haskell_dir) --main-module STORAGE-VERIFICATION > $@

tests/specs/examples/empty-bin-runtime.k: tests/specs/examples/Empty.sol $(KEVM_LIB)/$(haskell_kompiled) poetry
	$(KEVM) solc-to-k $< Empty $(KEVM_OPTS) --verbose --definition $(KEVM_LIB)/$(haskell_dir) --main-module EMPTY-VERIFICATION > $@

.SECONDEXPANSION:
tests/specs/%.prove: tests/specs/% tests/specs/$$(firstword $$(subst /, ,$$*))/$$(KPROVE_FILE)/$(TEST_SYMBOLIC_BACKEND)/timestamp
	$(POETRY_RUN) $(KEVM) prove $< $(KEVM_OPTS) --backend $(TEST_SYMBOLIC_BACKEND) $(KPROVE_OPTS) \
	    --definition tests/specs/$(firstword $(subst /, ,$*))/$(KPROVE_FILE)/$(TEST_SYMBOLIC_BACKEND)

tests/specs/%/timestamp: tests/specs/$$(firstword $$(subst /, ,$$*))/$$(KPROVE_FILE).$$(KPROVE_EXT) $(kevm_includes) $(plugin_includes)
	$(KOMPILE)                                                                                                  \
		$<                                                                                                      \
		--target $(word 3, $(subst /, , $*))                                                                    \
	    --output-definition tests/specs/$(firstword $(subst /, ,$*))/$(KPROVE_FILE)/$(word 3, $(subst /, , $*)) \
	    --main-module $(KPROVE_MODULE)                                                                          \
	    --syntax-module $(KPROVE_MODULE)                                                                        \
	    $(KOMPILE_OPTS)

tests/%.search: tests/%
	$(KEVM) search $< "<statusCode> EVMC_INVALID_INSTRUCTION </statusCode>" $(KEVM_OPTS) $(KSEARCH_OPTS) --backend $(TEST_SYMBOLIC_BACKEND) > $@-out
	$(CHECK) $@-out $@-expected
	$(KEEP_OUTPUTS) || rm -rf $@-out

# Smoke Tests

smoke_tests_run = tests/ethereum-tests/LegacyTests/Constantinople/VMTests/vmArithmeticTest/add0.json      \
                  tests/ethereum-tests/LegacyTests/Constantinople/VMTests/vmIOandFlowOperations/pop1.json \
                  tests/interactive/sumTo10.evm

smoke_tests_prove=tests/specs/erc20/ds/transfer-failure-1-a-spec.k

# Conformance Tests

tests/ethereum-tests/%.json: tests/ethereum-tests/make.timestamp

slow_conformance_tests    = $(shell cat tests/slow.$(TEST_CONCRETE_BACKEND))    # timeout after 20s
failing_conformance_tests = $(shell cat tests/failing.$(TEST_CONCRETE_BACKEND))

test-all-conformance: test-all-vm test-all-bchain
test-rest-conformance: test-rest-vm test-rest-bchain
test-slow-conformance: $(slow_conformance_tests:=.run)
test-failing-conformance: $(failing_conformance_tests:=.run)
test-conformance: test-vm test-bchain

all_vm_tests     = $(wildcard tests/ethereum-tests/LegacyTests/Constantinople/VMTests/*/*.json)
quick_vm_tests   = $(filter-out $(slow_conformance_tests), $(all_vm_tests))
passing_vm_tests = $(filter-out $(failing_conformance_tests), $(quick_vm_tests))
rest_vm_tests    = $(filter-out $(passing_vm_tests), $(all_vm_tests))

test-all-vm: $(all_vm_tests:=.run)
test-rest-vm: $(rest_vm_tests:=.run)
test-vm: $(passing_vm_tests:=.run)

all_bchain_tests     = $(wildcard tests/ethereum-tests/BlockchainTests/GeneralStateTests/*/*.json)                            \
                       $(wildcard tests/ethereum-tests/LegacyTests/Constantinople/BlockchainTests/GeneralStateTests/*/*.json)
quick_bchain_tests   = $(filter-out $(slow_conformance_tests), $(all_bchain_tests))
passing_bchain_tests = $(filter-out $(failing_conformance_tests), $(quick_bchain_tests))
rest_bchain_tests    = $(filter-out $(passing_bchain_tests), $(all_bchain_tests))

test-all-bchain: $(all_bchain_tests:=.run)
test-rest-bchain: $(rest_bchain_tests:=.run)
test-bchain: $(passing_bchain_tests:=.run)

# Proof Tests

prove_specs_dir          := tests/specs
prove_failing_tests      := $(shell cat tests/failing-symbolic.$(TEST_SYMBOLIC_BACKEND))
prove_pyk_failing_tests  := $(shell cat tests/failing-symbolic.pyk)
prove_slow_tests         := $(shell cat tests/slow.$(TEST_SYMBOLIC_BACKEND))
prove_skip_tests         := $(prove_failing_tests) $(prove_slow_tests)
prove_benchmarks_tests   := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/benchmarks/*-spec.k))
prove_functional_tests   := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/functional/*-spec.k))
prove_opcodes_tests      := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/opcodes/*-spec.k))
prove_erc20_tests        := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/erc20/*/*-spec.k))
prove_bihu_tests         := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/bihu/*-spec.k))
prove_examples_tests     := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/examples/*-spec.k) $(wildcard $(prove_specs_dir)/examples/*-spec.md))
prove_mcd_tests          := $(filter-out $(prove_skip_tests), $(wildcard $(prove_specs_dir)/mcd/*-spec.k))
prove_optimization_tests := $(filter-out $(prove_skip_tests), tests/specs/opcodes/evm-optimizations-spec.md)
prove_all_tests          := $(prove_benchmarks_tests) $(prove_functional_tests) $(prove_opcodes_tests) $(prove_erc20_tests) $(prove_bihu_tests) $(prove_examples_tests) $(prove_mcd_tests) $(prove_optimization_tests)
prove_pyk_tests          := $(filter-out $(prove_pyk_failing_tests), $(prove_all_tests))
prove_smoke_tests        := $(shell cat tests/specs/smoke)

## best-effort list of prove kompiled definitions to produce ahead of time
prove_haskell_definitions :=                                                              \
                             tests/specs/benchmarks/functional-spec/haskell/timestamp     \
                             tests/specs/benchmarks/verification/haskell/timestamp        \
                             tests/specs/bihu/functional-spec/haskell/timestamp           \
                             tests/specs/bihu/verification/haskell/timestamp              \
                             tests/specs/erc20/verification/haskell/timestamp             \
                             tests/specs/examples/erc20-spec/haskell/timestamp            \
                             tests/specs/examples/erc721-spec/haskell/timestamp           \
                             tests/specs/examples/storage-spec/haskell/timestamp          \
                             tests/specs/examples/solidity-code-spec/haskell/timestamp    \
                             tests/specs/examples/sum-to-n-spec/haskell/timestamp         \
                             tests/specs/examples/sum-to-n-foundry-spec/haskell/timestamp \
                             tests/specs/functional/infinite-gas-spec/haskell/timestamp   \
                             tests/specs/functional/lemmas-no-smt-spec/haskell/timestamp  \
                             tests/specs/functional/lemmas-spec/haskell/timestamp         \
                             tests/specs/functional/merkle-spec/haskell/timestamp         \
                             tests/specs/functional/storageRoot-spec/haskell/timestamp    \
                             tests/specs/mcd/functional-spec/haskell/timestamp            \
                             tests/specs/mcd/verification/haskell/timestamp               \
                             tests/specs/opcodes/evm-optimizations-spec/haskell/timestamp
build-prove-haskell: $(KEVM_BIN)/kevm $(prove_haskell_definitions)
build-prove: $(prove_haskell_definitions)

test-prove: test-prove-benchmarks test-prove-functional test-prove-opcodes test-prove-erc20 test-prove-bihu test-prove-examples test-prove-mcd test-prove-optimizations
test-prove-benchmarks:    $(prove_benchmarks_tests:=.prove)
test-prove-functional:    $(prove_functional_tests:=.prove)
test-prove-opcodes:       $(prove_opcodes_tests:=.prove)
test-prove-erc20:         $(prove_erc20_tests:=.prove)
test-prove-bihu:          $(prove_bihu_tests:=.prove)
test-prove-examples:      $(prove_examples_tests:=.prove)
test-prove-mcd:           $(prove_mcd_tests:=.prove)
test-prove-optimizations: $(prove_optimization_tests:=.prove)
test-prove-smoke:         $(prove_smoke_tests:=.prove)

test-failing-prove: $(prove_failing_tests:=.prove)

test-klab-prove: KPROVE_OPTS += --debugger
test-klab-prove: $(smoke_tests_prove:=.prove)

$(prove_pyk_tests:=.prove): KPROVE_OPTS += --pyk --max-depth 1000 --verbose

# to generate optimizations.md, run: ./optimizer/optimize.sh &> output
tests/specs/opcodes/evm-optimizations-spec.md: include/kframework/optimizations.md
	cat $< | sed 's/^rule/claim/' | sed 's/EVM-OPTIMIZATIONS/EVM-OPTIMIZATIONS-SPEC/' | grep -v 'priority(40)' > $@

# Parse Tests

parse_tests:=$(wildcard tests/interactive/*.json) \
             $(wildcard tests/interactive/*.evm)

test-parse: $(parse_tests:=.parse)
	echo $(parse_tests)

# Failing correctly tests

failure_tests:=$(wildcard tests/failing/*.json)

test-failure: $(failure_tests:=.run-expected)

# kevm-pyk Tests

kevm_pyk_tests :=                                                                                              \
                  tests/interactive/vmLogTest/log3.json.gst-to-kore.check                                      \
                  tests/ethereum-tests/BlockchainTests/GeneralStateTests/VMTests/vmArithmeticTest/add.json.run \
                  tests/specs/examples/empty-bin-runtime.k                                                     \
                  tests/specs/examples/erc20-bin-runtime.k                                                     \
                  tests/specs/examples/erc721-bin-runtime.k

test-kevm-pyk: KEVM_OPTS += --pyk --verbose
test-kevm-pyk: KEVM := $(POETRY_RUN) $(KEVM)
test-kevm-pyk: $(kevm_pyk_tests) poetry

# Interactive Tests

test-interactive: test-interactive-run test-interactive-prove test-interactive-search test-interactive-help

test-interactive-run: $(smoke_tests_run:=.run-interactive)
test-interactive-prove: $(smoke_tests_prove:=.prove)

search_tests:=$(wildcard tests/interactive/search/*.evm)
test-interactive-search: $(search_tests:=.search)

test-interactive-help:
	$(KEVM) help

proto_tester := $(LOCAL_BIN)/proto_tester
proto-tester: $(proto_tester)
$(proto_tester): tests/vm/proto_tester.cpp
	@mkdir -p $(LOCAL_BIN)
	$(CXX) -I $(LOCAL_LIB)/proto $(protobuf_out) $< -o $@ -lprotobuf -lpthread

node_tests:=$(wildcard tests/vm/*.bin)
test-node: $(node_tests:=.run-node)

tests/vm/%.run-node: tests/vm/%.expected $(KEVM_BIN)/kevm-vm $(proto_tester)
	bash -c " \
	  kevm-vm 8888 127.0.0.1 & \
	  while ! netcat -z 127.0.0.1 8888; do sleep 0.1; done; \
	  netcat -N 127.0.0.1 8888 < tests/vm/$* > tests/vm/$*.out; \
	  kill %kevm-vm || true"
	$(proto_tester) $< tests/vm/$*.out

# Media
# -----

media: media-pdf

### Media generated PDFs

media_pdfs := 201710-presentation-devcon3                          \
              201801-presentation-csf                              \
              201905-exercise-k-workshop                           \
              201908-trufflecon-workshop 201908-trufflecon-firefly

media/%.pdf: media/%.md media/citations.md
	@mkdir -p $(dir $@)
	cat $^ | pandoc --from markdown --filter pandoc-citeproc --to beamer --output $@

media-pdf: $(patsubst %, media/%.pdf, $(media_pdfs))

metropolis-theme: $(BUILD_DIR)/media/metropolis/beamerthememetropolis.sty

$(BUILD_DIR)/media/metropolis/beamerthememetropolis.sty:
	cd $(dir $@) && $(MAKE)
