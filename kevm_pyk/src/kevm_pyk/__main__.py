import argparse
import json
import sys

from pyk.cli_utils import dir_path, file_path

from .kevm import KEVM
from .solc_to_k import gen_spec_modules, solc_compile, solc_to_k


def main():
    sys.setrecursionlimit(15000000)
    parser = create_argument_parser()
    args = parser.parse_args()

    if args.command == 'compile':
        res = solc_compile(args.contract_file)
        print(json.dumps(res))

    elif args.command in ['solc-to-k', 'gen-spec-modules', 'prove']:

        if 'definition_dir' not in args:
            raise ValueError(f'Must provide --definition argument to {args.command}!')
        kevm = KEVM(args['definition_dir'])

        if args.command == 'solc-to-k':
            res = solc_to_k(kevm, args.contract_file, args.contract_name, args.generate_storage)
            print(res)

        elif args.command == 'gen-spec-modules':
            res = gen_spec_modules(kevm, args.spec_module_name)
            print(res)

        elif args.command == 'prove':
            res = prove(kevm)
            print(res)

    else:
        assert False


def prove(kevm: KEVM) -> str:
    return ""


def create_argument_parser():
    parser = argparse.ArgumentParser(prog='python3 -m kevm_pyk')
    parser.add_argument('--definition', type=dir_path, dest='definition_dir', help='Path to definition to use.')
    command_parser = parser.add_subparsers(dest='command', required=True)

    solc_subparser = command_parser.add_parser('compile', help='Generate combined JSON with solc compilation results.')
    solc_subparser.add_argument('contract_file', type=file_path, help='Path to contract file.')

    solc_to_k_subparser = command_parser.add_parser('solc-to-k', help='Output helper K definition for given JSON output from solc compiler.')
    solc_to_k_subparser.add_argument('contract_file', type=file_path, help='Path to contract file.')
    solc_to_k_subparser.add_argument('contract_name', type=str, help='Name of contract to generate K helpers for.')
    solc_to_k_subparser.add_argument('--no-storage-slots', dest='generate_storage', default=True, action='store_false', help='Do not generate productions and rules for accessing storage slots')

    gen_spec_modules_subparser = command_parser.add_parser('gen-spec-modules', help='Output helper K definition for given JSON output from solc compiler.')
    gen_spec_modules_subparser.add_argument('spec_module_name', type=str, help='Name of module containing all the generated specs.')

    return parser


if __name__ == "__main__":
    main()
