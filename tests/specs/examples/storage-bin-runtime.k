requires "edsl.md"

module Storage-CONTRACT
    imports public EDSL
    
    syntax Contract ::= S2KStorageContract
    
    syntax S2KStorageContract ::= "S2KStorage" [symbol(contract_Storage)]
    
    rule  ( #binRuntime ( S2KStorage ) => #parseByteStack ( "0x608060405234801561001057600080fd5b50600436106103fc5760003560e01c80637288e87c11610215578063a03b52fd11610125578063d88ed1d7116100b8578063eb1b30d911610087578063eb1b30d914610b63578063f08d610314610b7f578063f616964a14610b9d578063f8be065114610bbb578063fc94ae0914610bd9576103fc565b8063d88ed1d714610aeb578063e0b1524f14610b09578063e2a4b2af14610b27578063e898852414610b45576103fc565b8063b4aadf23116100f4578063b4aadf2314610a73578063b6e3197e14610a91578063b8bf41b214610aaf578063c3ff504014610acd576103fc565b8063a03b52fd146109fb578063a7dbce1c14610a19578063a84631ba14610a37578063abac82bd14610a55576103fc565b806387d6ef18116101a857806391f9a0ef1161017757806391f9a0ef146109655780639375ab821461098357806398c2d5ee146109a157806399282470146109bf5780639b6a236f146109dd576103fc565b806387d6ef18146108ed57806389d70f951461090b5780638e2dc2cb146109295780638f56f49114610947576103fc565b80637ecc9e89116101e45780637ecc9e89146108755780637f2482961461089357806382266dbc146108b1578063848aefe7146108cf576103fc565b80637288e87c146107fd578063734b1e531461081b578063775a974214610839578063794d1dda14610857576103fc565b80633ed5a1b91161031057806350fa9586116102a35780636652754f116102725780636652754f146107675780636cd7c55d146107855780636deecdbe146107a35780636e92c39e146107c1578063712f4602146107df576103fc565b806350fa9586146106ef578063512c8e2f1461070d578063527400331461072b5780635507c8fa14610749576103fc565b806345d12877116102df57806345d128771461067757806345e6eb4314610695578063492bfa18146106b35780634d70c615146106d1576103fc565b80633ed5a1b9146105ff5780633ef9ce951461061d5780633f066ec31461063b57806343f9f4d014610659576103fc565b8063120d999f1161039357806326e05a9b1161036257806326e05a9b14610569578063377172b91461058757806337aa1527146105a557806338719ee5146105c35780633c2cfbae146105e1576103fc565b8063120d999f146104f157806313a8ebd51461050f578063157813861461052d578063184256ed1461054b576103fc565b80630abf5438116103cf5780630abf5438146104795780630b9031f7146104975780630db0d3a6146104b5578063118b7864146104d3576103fc565b806303d5c6a014610401578063060b4f311461041f578063062811381461043d57806309a407f61461045b575b600080fd5b610409610bf7565b60405161041691906113d1565b60405180910390f35b610427610c0a565b6040516104349190611412565b60405180910390f35b610445610c27565b6040516104529190611449565b60405180910390f35b610463610c3a565b6040516104709190611498565b60405180910390f35b610481610c65565b60405161048e91906114cf565b60405180910390f35b61049f610c78565b6040516104ac9190611506565b60405180910390f35b6104bd610c8b565b6040516104ca9190611554565b60405180910390f35b6104db610cb5565b6040516104e8919061158b565b60405180910390f35b6104f9610cc8565b60405161050691906115c5565b60405180910390f35b610517610cde565b6040516105249190611604565b60405180910390f35b610535610cf9565b604051610542919061164d565b60405180910390f35b610553610d1e565b604051610560919061169a565b60405180910390f35b610571610d47565b60405161057e91906116d1565b60405180910390f35b61058f610d5a565b60405161059c9190611705565b60405180910390f35b6105ad610d60565b6040516105ba919061173c565b60405180910390f35b6105cb610d73565b6040516105d89190611775565b60405180910390f35b6105e9610d88565b6040516105f691906117c0565b60405180910390f35b610607610daf565b60405161061491906117f7565b60405180910390f35b610625610dc2565b6040516106329190611835565b60405180910390f35b610643610ddc565b604051610650919061188a565b60405180910390f35b610661610e0d565b60405161066e91906118c1565b60405180910390f35b61067f610e20565b60405161068c91906118f8565b60405180910390f35b61069d610e33565b6040516106aa919061192f565b60405180910390f35b6106bb610e46565b6040516106c891906119e3565b60405180910390f35b6106d9610ed4565b6040516106e69190611a21565b60405180910390f35b6106f7610ee7565b6040516107049190611a58565b60405180910390f35b610715610efa565b6040516107229190611a8f565b60405180910390f35b610733610f0d565b6040516107409190611ad9565b60405180910390f35b610751610f33565b60405161075e9190611b10565b60405180910390f35b61076f610f44565b60405161077c9190611b47565b60405180910390f35b61078d610f57565b60405161079a9190611b7e565b60405180910390f35b6107ab610f6a565b6040516107b89190611bb4565b60405180910390f35b6107c9610f7b565b6040516107d69190611beb565b60405180910390f35b6107e7610f8e565b6040516107f49190611c5b565b60405180910390f35b61080561101c565b6040516108129190611c99565b60405180910390f35b61082361102f565b6040516108309190611ceb565b60405180910390f35b61084161105d565b60405161084e9190611d22565b60405180910390f35b61085f611070565b60405161086c9190611d5e565b60405180910390f35b61087d611088565b60405161088a9190611da4565b60405180910390f35b61089b6110aa565b6040516108a89190611ddf565b60405180910390f35b6108b96110c1565b6040516108c69190611e16565b60405180910390f35b6108d76110d4565b6040516108e49190611e6a565b60405180910390f35b6108f5611104565b6040516109029190611eaa565b60405180910390f35b610913611120565b6040516109209190611eee565b60405180910390f35b610931611140565b60405161093e9190611f26565b60405180910390f35b61094f611154565b60405161095c9190611f72565b60405180910390f35b61096d61117c565b60405161097a9190611fa9565b60405180910390f35b61098b61118f565b6040516109989190611fe0565b60405180910390f35b6109a96111a2565b6040516109b69190612023565b60405180910390f35b6109c76111c1565b6040516109d49190612076565b60405180910390f35b6109e56111f0565b6040516109f291906120ad565b60405180910390f35b610a03611203565b604051610a1091906120e4565b60405180910390f35b610a21611216565b604051610a2e9190612118565b60405180910390f35b610a3f61121c565b604051610a4c919061215a565b60405180910390f35b610a5d61123a565b604051610a6a9190612191565b60405180910390f35b610a7b61124d565b604051610a8891906121c8565b60405180910390f35b610a99611260565b604051610aa6919061220d565b60405180910390f35b610ab7611281565b604051610ac4919061224a565b60405180910390f35b610ad561129a565b604051610ae2919061229b565b60405180910390f35b610af36112c7565b604051610b0091906122eb565b60405180910390f35b610b116112f3565b604051610b1e9190612322565b60405180910390f35b610b2f611306565b604051610b3c9190612359565b60405180910390f35b610b4d611319565b604051610b5a9190612390565b60405180910390f35b610b7d6004803603810190610b7891906123dc565b61132c565b005b610b87611348565b604051610b949190612436565b60405180910390f35b610ba561136c565b604051610bb2919061246d565b60405180910390f35b610bc361137f565b604051610bd091906124b4565b60405180910390f35b610be16113a2565b604051610bee91906124eb565b60405180910390f35b601e60009054906101000a900460140b81565b600260009054906101000a90046affffffffffffffffffffff1681565b602360009054906101000a900460190b81565b600d60009054906101000a900478ffffffffffffffffffffffffffffffffffffffffffffffffff1681565b601560039054906101000a900460020b81565b602760009054906101000a9004601d0b81565b600c60009054906101000a900477ffffffffffffffffffffffffffffffffffffffffffffffff1681565b6015600f9054906101000a900460050b81565b600060079054906101000a900463ffffffff1681565b600160089054906101000a900468ffffffffffffffffff1681565b600760009054906101000a900472ffffffffffffffffffffffffffffffffffffff1681565b600b60009054906101000a900476ffffffffffffffffffffffffffffffffffffffffffffff1681565b601560069054906101000a900460030b81565b60295481565b602060009054906101000a900460160b81565b600060049054906101000a900462ffffff1681565b600960009054906101000a900474ffffffffffffffffffffffffffffffffffffffffff1681565b602560009054906101000a9004601b0b81565b600160009054906101000a900467ffffffffffffffff1681565b601360009054906101000a90047effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b6017600b9054906101000a9004600b0b81565b6019600f9054906101000a9004600f0b81565b602860009054906101000a9004601e0b81565b602a8054610e5390612535565b80601f0160208091040260200160405190810160405280929190818152602001828054610e7f90612535565b8015610ecc5780601f10610ea157610100808354040283529160200191610ecc565b820191906000526020600020905b815481529060010190602001808311610eaf57829003601f168201915b505050505081565b602660009054906101000a9004601c0b81565b601660089054906101000a900460080b81565b6018600d9054906101000a9004600d0b81565b600860009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60158054906101000a900460060b81565b601560019054906101000a900460010b81565b601660009054906101000a900460070b81565b60008054906101000a900460ff1681565b601560009054906101000a900460000b81565b602b8054610f9b90612535565b80601f0160208091040260200160405190810160405280929190818152602001828054610fc790612535565b80156110145780601f10610fe957610100808354040283529160200191611014565b820191906000526020600020905b815481529060010190602001808311610ff757829003601f168201915b505050505081565b601a60009054906101000a900460100b81565b601060009054906101000a90047bffffffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b602260009054906101000a900460180b81565b600060109054906101000a900465ffffffffffff1681565b6004600f9054906101000a90046fffffffffffffffffffffffffffffffff1681565b6000600b9054906101000a900464ffffffffff1681565b601c60009054906101000a900460120b81565b601260009054906101000a90047dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b600160119054906101000a900469ffffffffffffffffffff1681565b6003600d9054906101000a90046dffffffffffffffffffffffffffff1681565b600060029054906101000a900461ffff1681565b600a60009054906101000a900475ffffffffffffffffffffffffffffffffffffffffffff1681565b601960009054906101000a9004600e0b81565b601f60009054906101000a900460150b81565b600360009054906101000a90046cffffffffffffffffffffffffff1681565b601160009054906101000a90047cffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b601660119054906101000a900460090b81565b6015600a9054906101000a900460040b81565b60145481565b6002600b9054906101000a90046bffffffffffffffffffffffff1681565b601d60009054906101000a900460130b81565b601b60009054906101000a900460110b81565b600460009054906101000a90046effffffffffffffffffffffffffffff1681565b600060169054906101000a900466ffffffffffffff1681565b600f60009054906101000a90047affffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b600e60009054906101000a900479ffffffffffffffffffffffffffffffffffffffffffffffffffff1681565b601860009054906101000a9004600c0b81565b600060019054906101000a900460ff1681565b602160009054906101000a900460170b81565b806000806101000a81548160ff02191690831515021790555050565b600660009054906101000a900471ffffffffffffffffffffffffffffffffffff1681565b602460009054906101000a9004601a0b81565b600560009054906101000a900470ffffffffffffffffffffffffffffffffff1681565b601760009054906101000a9004600a0b81565b60008160140b9050919050565b6113cb816113b5565b82525050565b60006020820190506113e660008301846113c2565b92915050565b60006affffffffffffffffffffff82169050919050565b61140c816113ec565b82525050565b60006020820190506114276000830184611403565b92915050565b60008160190b9050919050565b6114438161142d565b82525050565b600060208201905061145e600083018461143a565b92915050565b600078ffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b61149281611464565b82525050565b60006020820190506114ad6000830184611489565b92915050565b60008160020b9050919050565b6114c9816114b3565b82525050565b60006020820190506114e460008301846114c0565b92915050565b600081601d0b9050919050565b611500816114ea565b82525050565b600060208201905061151b60008301846114f7565b92915050565b600077ffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b61154e81611521565b82525050565b60006020820190506115696000830184611545565b92915050565b60008160050b9050919050565b6115858161156f565b82525050565b60006020820190506115a0600083018461157c565b92915050565b600063ffffffff82169050919050565b6115bf816115a6565b82525050565b60006020820190506115da60008301846115b6565b92915050565b600068ffffffffffffffffff82169050919050565b6115fe816115e0565b82525050565b600060208201905061161960008301846115f5565b92915050565b600072ffffffffffffffffffffffffffffffffffffff82169050919050565b6116478161161f565b82525050565b6000602082019050611662600083018461163e565b92915050565b600076ffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b61169481611668565b82525050565b60006020820190506116af600083018461168b565b92915050565b60008160030b9050919050565b6116cb816116b5565b82525050565b60006020820190506116e660008301846116c2565b92915050565b6000819050919050565b6116ff816116ec565b82525050565b600060208201905061171a60008301846116f6565b92915050565b60008160160b9050919050565b61173681611720565b82525050565b6000602082019050611751600083018461172d565b92915050565b600062ffffff82169050919050565b61176f81611757565b82525050565b600060208201905061178a6000830184611766565b92915050565b600074ffffffffffffffffffffffffffffffffffffffffff82169050919050565b6117ba81611790565b82525050565b60006020820190506117d560008301846117b1565b92915050565b600081601b0b9050919050565b6117f1816117db565b82525050565b600060208201905061180c60008301846117e8565b92915050565b600067ffffffffffffffff82169050919050565b61182f81611812565b82525050565b600060208201905061184a6000830184611826565b92915050565b60007effffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b61188481611850565b82525050565b600060208201905061189f600083018461187b565b92915050565b600081600b0b9050919050565b6118bb816118a5565b82525050565b60006020820190506118d660008301846118b2565b92915050565b600081600f0b9050919050565b6118f2816118dc565b82525050565b600060208201905061190d60008301846118e9565b92915050565b600081601e0b9050919050565b61192981611913565b82525050565b60006020820190506119446000830184611920565b92915050565b600081519050919050565b600082825260208201905092915050565b60005b83811015611984578082015181840152602081019050611969565b83811115611993576000848401525b50505050565b6000601f19601f8301169050919050565b60006119b58261194a565b6119bf8185611955565b93506119cf818560208601611966565b6119d881611999565b840191505092915050565b600060208201905081810360008301526119fd81846119aa565b905092915050565b600081601c0b9050919050565b611a1b81611a05565b82525050565b6000602082019050611a366000830184611a12565b92915050565b60008160080b9050919050565b611a5281611a3c565b82525050565b6000602082019050611a6d6000830184611a49565b92915050565b600081600d0b9050919050565b611a8981611a73565b82525050565b6000602082019050611aa46000830184611a80565b92915050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b611ad381611aaa565b82525050565b6000602082019050611aee6000830184611aca565b92915050565b60008160060b9050919050565b611b0a81611af4565b82525050565b6000602082019050611b256000830184611b01565b92915050565b60008160010b9050919050565b611b4181611b2b565b82525050565b6000602082019050611b5c6000830184611b38565b92915050565b60008160070b9050919050565b611b7881611b62565b82525050565b6000602082019050611b936000830184611b6f565b92915050565b60008115159050919050565b611bae81611b99565b82525050565b6000602082019050611bc96000830184611ba5565b92915050565b60008160000b9050919050565b611be581611bcf565b82525050565b6000602082019050611c006000830184611bdc565b92915050565b600081519050919050565b600082825260208201905092915050565b6000611c2d82611c06565b611c378185611c11565b9350611c47818560208601611966565b611c5081611999565b840191505092915050565b60006020820190508181036000830152611c758184611c22565b905092915050565b60008160100b9050919050565b611c9381611c7d565b82525050565b6000602082019050611cae6000830184611c8a565b92915050565b60007bffffffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b611ce581611cb4565b82525050565b6000602082019050611d006000830184611cdc565b92915050565b60008160180b9050919050565b611d1c81611d06565b82525050565b6000602082019050611d376000830184611d13565b92915050565b600065ffffffffffff82169050919050565b611d5881611d3d565b82525050565b6000602082019050611d736000830184611d4f565b92915050565b60006fffffffffffffffffffffffffffffffff82169050919050565b611d9e81611d79565b82525050565b6000602082019050611db96000830184611d95565b92915050565b600064ffffffffff82169050919050565b611dd981611dbf565b82525050565b6000602082019050611df46000830184611dd0565b92915050565b60008160120b9050919050565b611e1081611dfa565b82525050565b6000602082019050611e2b6000830184611e07565b92915050565b60007dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b611e6481611e31565b82525050565b6000602082019050611e7f6000830184611e5b565b92915050565b600069ffffffffffffffffffff82169050919050565b611ea481611e85565b82525050565b6000602082019050611ebf6000830184611e9b565b92915050565b60006dffffffffffffffffffffffffffff82169050919050565b611ee881611ec5565b82525050565b6000602082019050611f036000830184611edf565b92915050565b600061ffff82169050919050565b611f2081611f09565b82525050565b6000602082019050611f3b6000830184611f17565b92915050565b600075ffffffffffffffffffffffffffffffffffffffffffff82169050919050565b611f6c81611f41565b82525050565b6000602082019050611f876000830184611f63565b92915050565b600081600e0b9050919050565b611fa381611f8d565b82525050565b6000602082019050611fbe6000830184611f9a565b92915050565b60008160150b9050919050565b611fda81611fc4565b82525050565b6000602082019050611ff56000830184611fd1565b92915050565b60006cffffffffffffffffffffffffff82169050919050565b61201d81611ffb565b82525050565b60006020820190506120386000830184612014565b92915050565b60007cffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b6120708161203e565b82525050565b600060208201905061208b6000830184612067565b92915050565b60008160090b9050919050565b6120a781612091565b82525050565b60006020820190506120c2600083018461209e565b92915050565b60008160040b9050919050565b6120de816120c8565b82525050565b60006020820190506120f960008301846120d5565b92915050565b6000819050919050565b612112816120ff565b82525050565b600060208201905061212d6000830184612109565b92915050565b60006bffffffffffffffffffffffff82169050919050565b61215481612133565b82525050565b600060208201905061216f600083018461214b565b92915050565b60008160130b9050919050565b61218b81612175565b82525050565b60006020820190506121a66000830184612182565b92915050565b60008160110b9050919050565b6121c2816121ac565b82525050565b60006020820190506121dd60008301846121b9565b92915050565b60006effffffffffffffffffffffffffffff82169050919050565b612207816121e3565b82525050565b600060208201905061222260008301846121fe565b92915050565b600066ffffffffffffff82169050919050565b61224481612228565b82525050565b600060208201905061225f600083018461223b565b92915050565b60007affffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b61229581612265565b82525050565b60006020820190506122b0600083018461228c565b92915050565b600079ffffffffffffffffffffffffffffffffffffffffffffffffffff82169050919050565b6122e5816122b6565b82525050565b600060208201905061230060008301846122dc565b92915050565b600081600c0b9050919050565b61231c81612306565b82525050565b60006020820190506123376000830184612313565b92915050565b600060ff82169050919050565b6123538161233d565b82525050565b600060208201905061236e600083018461234a565b92915050565b60008160170b9050919050565b61238a81612374565b82525050565b60006020820190506123a56000830184612381565b92915050565b600080fd5b6123b981611b99565b81146123c457600080fd5b50565b6000813590506123d6816123b0565b92915050565b6000602082840312156123f2576123f16123ab565b5b6000612400848285016123c7565b91505092915050565b600071ffffffffffffffffffffffffffffffffffff82169050919050565b61243081612409565b82525050565b600060208201905061244b6000830184612427565b92915050565b600081601a0b9050919050565b61246781612451565b82525050565b6000602082019050612482600083018461245e565b92915050565b600070ffffffffffffffffffffffffffffffffff82169050919050565b6124ae81612488565b82525050565b60006020820190506124c960008301846124a5565b92915050565b600081600a0b9050919050565b6124e5816124cf565b82525050565b600060208201905061250060008301846124dc565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052602260045260246000fd5b6000600282049050600182168061254d57607f821691505b6020821081036125605761255f612506565b5b5091905056fea26469706673582212209d89f7186a163d8a4087cae2caff77f1894ba5c5c5c78eacabc4b169156d4fa064736f6c634300080d0033" ) )
      
    
    syntax Field ::= StorageField
    
    syntax StorageField ::= "myBool" [symbol(field_Storage_myBool)]
    
    syntax StorageField ::= "myUint8" [symbol(field_Storage_myUint8)]
    
    syntax StorageField ::= "myUint16" [symbol(field_Storage_myUint16)]
    
    syntax StorageField ::= "myUint24" [symbol(field_Storage_myUint24)]
    
    syntax StorageField ::= "myUint32" [symbol(field_Storage_myUint32)]
    
    syntax StorageField ::= "myUint40" [symbol(field_Storage_myUint40)]
    
    syntax StorageField ::= "myUint48" [symbol(field_Storage_myUint48)]
    
    syntax StorageField ::= "myUint56" [symbol(field_Storage_myUint56)]
    
    syntax StorageField ::= "myUint64" [symbol(field_Storage_myUint64)]
    
    syntax StorageField ::= "myUint72" [symbol(field_Storage_myUint72)]
    
    syntax StorageField ::= "myUint80" [symbol(field_Storage_myUint80)]
    
    syntax StorageField ::= "myUint88" [symbol(field_Storage_myUint88)]
    
    syntax StorageField ::= "myUint96" [symbol(field_Storage_myUint96)]
    
    syntax StorageField ::= "myUint104" [symbol(field_Storage_myUint104)]
    
    syntax StorageField ::= "myUint112" [symbol(field_Storage_myUint112)]
    
    syntax StorageField ::= "myUint120" [symbol(field_Storage_myUint120)]
    
    syntax StorageField ::= "myUint128" [symbol(field_Storage_myUint128)]
    
    syntax StorageField ::= "myUint136" [symbol(field_Storage_myUint136)]
    
    syntax StorageField ::= "myUint144" [symbol(field_Storage_myUint144)]
    
    syntax StorageField ::= "myUint152" [symbol(field_Storage_myUint152)]
    
    syntax StorageField ::= "myUint160" [symbol(field_Storage_myUint160)]
    
    syntax StorageField ::= "myUint168" [symbol(field_Storage_myUint168)]
    
    syntax StorageField ::= "myUint176" [symbol(field_Storage_myUint176)]
    
    syntax StorageField ::= "myUint184" [symbol(field_Storage_myUint184)]
    
    syntax StorageField ::= "myUint192" [symbol(field_Storage_myUint192)]
    
    syntax StorageField ::= "myUint200" [symbol(field_Storage_myUint200)]
    
    syntax StorageField ::= "myUint208" [symbol(field_Storage_myUint208)]
    
    syntax StorageField ::= "myUint216" [symbol(field_Storage_myUint216)]
    
    syntax StorageField ::= "myUint224" [symbol(field_Storage_myUint224)]
    
    syntax StorageField ::= "myUint232" [symbol(field_Storage_myUint232)]
    
    syntax StorageField ::= "myUint240" [symbol(field_Storage_myUint240)]
    
    syntax StorageField ::= "myUint248" [symbol(field_Storage_myUint248)]
    
    syntax StorageField ::= "myUint256" [symbol(field_Storage_myUint256)]
    
    syntax StorageField ::= "myInt8" [symbol(field_Storage_myInt8)]
    
    syntax StorageField ::= "myInt16" [symbol(field_Storage_myInt16)]
    
    syntax StorageField ::= "myInt24" [symbol(field_Storage_myInt24)]
    
    syntax StorageField ::= "myInt32" [symbol(field_Storage_myInt32)]
    
    syntax StorageField ::= "myInt40" [symbol(field_Storage_myInt40)]
    
    syntax StorageField ::= "myInt48" [symbol(field_Storage_myInt48)]
    
    syntax StorageField ::= "myInt56" [symbol(field_Storage_myInt56)]
    
    syntax StorageField ::= "myInt64" [symbol(field_Storage_myInt64)]
    
    syntax StorageField ::= "myInt72" [symbol(field_Storage_myInt72)]
    
    syntax StorageField ::= "myInt80" [symbol(field_Storage_myInt80)]
    
    syntax StorageField ::= "myInt88" [symbol(field_Storage_myInt88)]
    
    syntax StorageField ::= "myInt96" [symbol(field_Storage_myInt96)]
    
    syntax StorageField ::= "myInt104" [symbol(field_Storage_myInt104)]
    
    syntax StorageField ::= "myInt112" [symbol(field_Storage_myInt112)]
    
    syntax StorageField ::= "myInt120" [symbol(field_Storage_myInt120)]
    
    syntax StorageField ::= "myInt128" [symbol(field_Storage_myInt128)]
    
    syntax StorageField ::= "myInt136" [symbol(field_Storage_myInt136)]
    
    syntax StorageField ::= "myInt144" [symbol(field_Storage_myInt144)]
    
    syntax StorageField ::= "myInt152" [symbol(field_Storage_myInt152)]
    
    syntax StorageField ::= "myInt160" [symbol(field_Storage_myInt160)]
    
    syntax StorageField ::= "myInt168" [symbol(field_Storage_myInt168)]
    
    syntax StorageField ::= "myInt176" [symbol(field_Storage_myInt176)]
    
    syntax StorageField ::= "myInt184" [symbol(field_Storage_myInt184)]
    
    syntax StorageField ::= "myInt192" [symbol(field_Storage_myInt192)]
    
    syntax StorageField ::= "myInt200" [symbol(field_Storage_myInt200)]
    
    syntax StorageField ::= "myInt208" [symbol(field_Storage_myInt208)]
    
    syntax StorageField ::= "myInt216" [symbol(field_Storage_myInt216)]
    
    syntax StorageField ::= "myInt224" [symbol(field_Storage_myInt224)]
    
    syntax StorageField ::= "myInt232" [symbol(field_Storage_myInt232)]
    
    syntax StorageField ::= "myInt240" [symbol(field_Storage_myInt240)]
    
    syntax StorageField ::= "myInt248" [symbol(field_Storage_myInt248)]
    
    syntax StorageField ::= "myInt256" [symbol(field_Storage_myInt256)]
    
    syntax StorageField ::= "myString" [symbol(field_Storage_myString)]
    
    syntax StorageField ::= "myBytes" [symbol(field_Storage_myBytes)]
    
    syntax StorageField ::= "myUint128s" [symbol(field_Storage_myUint128s)]
    
    syntax StorageField ::= "myUint64s" [symbol(field_Storage_myUint64s)]
    
    syntax StorageField ::= "myFoo" [symbol(field_Storage_myFoo)]
    
    syntax StorageField ::= "myFoos" [symbol(field_Storage_myFoos)]
    
    rule  ( #loc ( S2KStorage . myBool ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint8 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint16 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint24 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint32 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint40 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint48 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint56 ) => 0 )
      
    
    rule  ( #loc ( S2KStorage . myUint64 ) => 1 )
      
    
    rule  ( #loc ( S2KStorage . myUint72 ) => 1 )
      
    
    rule  ( #loc ( S2KStorage . myUint80 ) => 1 )
      
    
    rule  ( #loc ( S2KStorage . myUint88 ) => 2 )
      
    
    rule  ( #loc ( S2KStorage . myUint96 ) => 2 )
      
    
    rule  ( #loc ( S2KStorage . myUint104 ) => 3 )
      
    
    rule  ( #loc ( S2KStorage . myUint112 ) => 3 )
      
    
    rule  ( #loc ( S2KStorage . myUint120 ) => 4 )
      
    
    rule  ( #loc ( S2KStorage . myUint128 ) => 4 )
      
    
    rule  ( #loc ( S2KStorage . myUint136 ) => 5 )
      
    
    rule  ( #loc ( S2KStorage . myUint144 ) => 6 )
      
    
    rule  ( #loc ( S2KStorage . myUint152 ) => 7 )
      
    
    rule  ( #loc ( S2KStorage . myUint160 ) => 8 )
      
    
    rule  ( #loc ( S2KStorage . myUint168 ) => 9 )
      
    
    rule  ( #loc ( S2KStorage . myUint176 ) => 10 )
      
    
    rule  ( #loc ( S2KStorage . myUint184 ) => 11 )
      
    
    rule  ( #loc ( S2KStorage . myUint192 ) => 12 )
      
    
    rule  ( #loc ( S2KStorage . myUint200 ) => 13 )
      
    
    rule  ( #loc ( S2KStorage . myUint208 ) => 14 )
      
    
    rule  ( #loc ( S2KStorage . myUint216 ) => 15 )
      
    
    rule  ( #loc ( S2KStorage . myUint224 ) => 16 )
      
    
    rule  ( #loc ( S2KStorage . myUint232 ) => 17 )
      
    
    rule  ( #loc ( S2KStorage . myUint240 ) => 18 )
      
    
    rule  ( #loc ( S2KStorage . myUint248 ) => 19 )
      
    
    rule  ( #loc ( S2KStorage . myUint256 ) => 20 )
      
    
    rule  ( #loc ( S2KStorage . myInt8 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt16 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt24 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt32 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt40 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt48 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt56 ) => 21 )
      
    
    rule  ( #loc ( S2KStorage . myInt64 ) => 22 )
      
    
    rule  ( #loc ( S2KStorage . myInt72 ) => 22 )
      
    
    rule  ( #loc ( S2KStorage . myInt80 ) => 22 )
      
    
    rule  ( #loc ( S2KStorage . myInt88 ) => 23 )
      
    
    rule  ( #loc ( S2KStorage . myInt96 ) => 23 )
      
    
    rule  ( #loc ( S2KStorage . myInt104 ) => 24 )
      
    
    rule  ( #loc ( S2KStorage . myInt112 ) => 24 )
      
    
    rule  ( #loc ( S2KStorage . myInt120 ) => 25 )
      
    
    rule  ( #loc ( S2KStorage . myInt128 ) => 25 )
      
    
    rule  ( #loc ( S2KStorage . myInt136 ) => 26 )
      
    
    rule  ( #loc ( S2KStorage . myInt144 ) => 27 )
      
    
    rule  ( #loc ( S2KStorage . myInt152 ) => 28 )
      
    
    rule  ( #loc ( S2KStorage . myInt160 ) => 29 )
      
    
    rule  ( #loc ( S2KStorage . myInt168 ) => 30 )
      
    
    rule  ( #loc ( S2KStorage . myInt176 ) => 31 )
      
    
    rule  ( #loc ( S2KStorage . myInt184 ) => 32 )
      
    
    rule  ( #loc ( S2KStorage . myInt192 ) => 33 )
      
    
    rule  ( #loc ( S2KStorage . myInt200 ) => 34 )
      
    
    rule  ( #loc ( S2KStorage . myInt208 ) => 35 )
      
    
    rule  ( #loc ( S2KStorage . myInt216 ) => 36 )
      
    
    rule  ( #loc ( S2KStorage . myInt224 ) => 37 )
      
    
    rule  ( #loc ( S2KStorage . myInt232 ) => 38 )
      
    
    rule  ( #loc ( S2KStorage . myInt240 ) => 39 )
      
    
    rule  ( #loc ( S2KStorage . myInt248 ) => 40 )
      
    
    rule  ( #loc ( S2KStorage . myInt256 ) => 41 )
      
    
    rule  ( #loc ( S2KStorage . myString ) => 42 )
      
    
    rule  ( #loc ( S2KStorage . myBytes ) => 43 )
      
    
    rule  ( #loc ( S2KStorage . myUint128s ) => 44 )
      
    
    rule  ( #loc ( S2KStorage . myUint64s ) => 45 )
      
    
    rule  ( #loc ( S2KStorage . myFoo ) => 47 )
      
    
    rule  ( #loc ( S2KStorage . myFoos ) => 49 )
      
    
    syntax Bytes ::= S2KStorageContract "." S2KStorageMethod [function(), symbol(method_Storage)]
    
    syntax S2KStorageMethod ::= "S2KmyBool" "(" ")" [symbol(method_Storage_S2KmyBool_)]
    
    syntax S2KStorageMethod ::= "S2KmyBytes" "(" ")" [symbol(method_Storage_S2KmyBytes_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt104" "(" ")" [symbol(method_Storage_S2KmyInt104_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt112" "(" ")" [symbol(method_Storage_S2KmyInt112_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt120" "(" ")" [symbol(method_Storage_S2KmyInt120_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt128" "(" ")" [symbol(method_Storage_S2KmyInt128_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt136" "(" ")" [symbol(method_Storage_S2KmyInt136_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt144" "(" ")" [symbol(method_Storage_S2KmyInt144_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt152" "(" ")" [symbol(method_Storage_S2KmyInt152_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt16" "(" ")" [symbol(method_Storage_S2KmyInt16_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt160" "(" ")" [symbol(method_Storage_S2KmyInt160_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt168" "(" ")" [symbol(method_Storage_S2KmyInt168_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt176" "(" ")" [symbol(method_Storage_S2KmyInt176_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt184" "(" ")" [symbol(method_Storage_S2KmyInt184_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt192" "(" ")" [symbol(method_Storage_S2KmyInt192_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt200" "(" ")" [symbol(method_Storage_S2KmyInt200_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt208" "(" ")" [symbol(method_Storage_S2KmyInt208_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt216" "(" ")" [symbol(method_Storage_S2KmyInt216_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt224" "(" ")" [symbol(method_Storage_S2KmyInt224_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt232" "(" ")" [symbol(method_Storage_S2KmyInt232_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt24" "(" ")" [symbol(method_Storage_S2KmyInt24_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt240" "(" ")" [symbol(method_Storage_S2KmyInt240_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt248" "(" ")" [symbol(method_Storage_S2KmyInt248_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt256" "(" ")" [symbol(method_Storage_S2KmyInt256_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt32" "(" ")" [symbol(method_Storage_S2KmyInt32_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt40" "(" ")" [symbol(method_Storage_S2KmyInt40_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt48" "(" ")" [symbol(method_Storage_S2KmyInt48_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt56" "(" ")" [symbol(method_Storage_S2KmyInt56_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt64" "(" ")" [symbol(method_Storage_S2KmyInt64_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt72" "(" ")" [symbol(method_Storage_S2KmyInt72_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt8" "(" ")" [symbol(method_Storage_S2KmyInt8_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt80" "(" ")" [symbol(method_Storage_S2KmyInt80_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt88" "(" ")" [symbol(method_Storage_S2KmyInt88_)]
    
    syntax S2KStorageMethod ::= "S2KmyInt96" "(" ")" [symbol(method_Storage_S2KmyInt96_)]
    
    syntax S2KStorageMethod ::= "S2KmyString" "(" ")" [symbol(method_Storage_S2KmyString_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint104" "(" ")" [symbol(method_Storage_S2KmyUint104_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint112" "(" ")" [symbol(method_Storage_S2KmyUint112_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint120" "(" ")" [symbol(method_Storage_S2KmyUint120_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint128" "(" ")" [symbol(method_Storage_S2KmyUint128_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint136" "(" ")" [symbol(method_Storage_S2KmyUint136_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint144" "(" ")" [symbol(method_Storage_S2KmyUint144_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint152" "(" ")" [symbol(method_Storage_S2KmyUint152_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint16" "(" ")" [symbol(method_Storage_S2KmyUint16_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint160" "(" ")" [symbol(method_Storage_S2KmyUint160_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint168" "(" ")" [symbol(method_Storage_S2KmyUint168_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint176" "(" ")" [symbol(method_Storage_S2KmyUint176_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint184" "(" ")" [symbol(method_Storage_S2KmyUint184_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint192" "(" ")" [symbol(method_Storage_S2KmyUint192_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint200" "(" ")" [symbol(method_Storage_S2KmyUint200_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint208" "(" ")" [symbol(method_Storage_S2KmyUint208_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint216" "(" ")" [symbol(method_Storage_S2KmyUint216_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint224" "(" ")" [symbol(method_Storage_S2KmyUint224_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint232" "(" ")" [symbol(method_Storage_S2KmyUint232_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint24" "(" ")" [symbol(method_Storage_S2KmyUint24_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint240" "(" ")" [symbol(method_Storage_S2KmyUint240_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint248" "(" ")" [symbol(method_Storage_S2KmyUint248_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint256" "(" ")" [symbol(method_Storage_S2KmyUint256_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint32" "(" ")" [symbol(method_Storage_S2KmyUint32_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint40" "(" ")" [symbol(method_Storage_S2KmyUint40_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint48" "(" ")" [symbol(method_Storage_S2KmyUint48_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint56" "(" ")" [symbol(method_Storage_S2KmyUint56_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint64" "(" ")" [symbol(method_Storage_S2KmyUint64_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint72" "(" ")" [symbol(method_Storage_S2KmyUint72_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint8" "(" ")" [symbol(method_Storage_S2KmyUint8_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint80" "(" ")" [symbol(method_Storage_S2KmyUint80_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint88" "(" ")" [symbol(method_Storage_S2KmyUint88_)]
    
    syntax S2KStorageMethod ::= "S2KmyUint96" "(" ")" [symbol(method_Storage_S2KmyUint96_)]
    
    syntax S2KStorageMethod ::= "S2KsetMyBool" "(" Int ":" "bool" ")" [symbol(method_Storage_S2KsetMyBool_bool)]
    
    rule  ( S2KStorage . S2KmyBool ( ) => #abiCallData ( "myBool" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyBytes ( ) => #abiCallData ( "myBytes" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt104 ( ) => #abiCallData ( "myInt104" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt112 ( ) => #abiCallData ( "myInt112" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt120 ( ) => #abiCallData ( "myInt120" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt128 ( ) => #abiCallData ( "myInt128" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt136 ( ) => #abiCallData ( "myInt136" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt144 ( ) => #abiCallData ( "myInt144" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt152 ( ) => #abiCallData ( "myInt152" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt16 ( ) => #abiCallData ( "myInt16" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt160 ( ) => #abiCallData ( "myInt160" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt168 ( ) => #abiCallData ( "myInt168" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt176 ( ) => #abiCallData ( "myInt176" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt184 ( ) => #abiCallData ( "myInt184" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt192 ( ) => #abiCallData ( "myInt192" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt200 ( ) => #abiCallData ( "myInt200" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt208 ( ) => #abiCallData ( "myInt208" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt216 ( ) => #abiCallData ( "myInt216" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt224 ( ) => #abiCallData ( "myInt224" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt232 ( ) => #abiCallData ( "myInt232" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt24 ( ) => #abiCallData ( "myInt24" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt240 ( ) => #abiCallData ( "myInt240" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt248 ( ) => #abiCallData ( "myInt248" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt256 ( ) => #abiCallData ( "myInt256" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt32 ( ) => #abiCallData ( "myInt32" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt40 ( ) => #abiCallData ( "myInt40" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt48 ( ) => #abiCallData ( "myInt48" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt56 ( ) => #abiCallData ( "myInt56" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt64 ( ) => #abiCallData ( "myInt64" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt72 ( ) => #abiCallData ( "myInt72" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt8 ( ) => #abiCallData ( "myInt8" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt80 ( ) => #abiCallData ( "myInt80" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt88 ( ) => #abiCallData ( "myInt88" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyInt96 ( ) => #abiCallData ( "myInt96" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyString ( ) => #abiCallData ( "myString" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint104 ( ) => #abiCallData ( "myUint104" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint112 ( ) => #abiCallData ( "myUint112" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint120 ( ) => #abiCallData ( "myUint120" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint128 ( ) => #abiCallData ( "myUint128" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint136 ( ) => #abiCallData ( "myUint136" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint144 ( ) => #abiCallData ( "myUint144" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint152 ( ) => #abiCallData ( "myUint152" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint16 ( ) => #abiCallData ( "myUint16" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint160 ( ) => #abiCallData ( "myUint160" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint168 ( ) => #abiCallData ( "myUint168" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint176 ( ) => #abiCallData ( "myUint176" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint184 ( ) => #abiCallData ( "myUint184" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint192 ( ) => #abiCallData ( "myUint192" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint200 ( ) => #abiCallData ( "myUint200" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint208 ( ) => #abiCallData ( "myUint208" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint216 ( ) => #abiCallData ( "myUint216" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint224 ( ) => #abiCallData ( "myUint224" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint232 ( ) => #abiCallData ( "myUint232" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint24 ( ) => #abiCallData ( "myUint24" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint240 ( ) => #abiCallData ( "myUint240" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint248 ( ) => #abiCallData ( "myUint248" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint256 ( ) => #abiCallData ( "myUint256" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint32 ( ) => #abiCallData ( "myUint32" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint40 ( ) => #abiCallData ( "myUint40" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint48 ( ) => #abiCallData ( "myUint48" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint56 ( ) => #abiCallData ( "myUint56" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint64 ( ) => #abiCallData ( "myUint64" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint72 ( ) => #abiCallData ( "myUint72" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint8 ( ) => #abiCallData ( "myUint8" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint80 ( ) => #abiCallData ( "myUint80" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint88 ( ) => #abiCallData ( "myUint88" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KmyUint96 ( ) => #abiCallData ( "myUint96" , .TypedArgs ) )
      
    
    rule  ( S2KStorage . S2KsetMyBool ( V0_newBool : bool ) => #abiCallData ( "setMyBool" , #bool ( V0_newBool ) , .TypedArgs ) )
       ensures #rangeBool ( V0_newBool )
      
    
    rule  ( selector ( "myBool()" ) => 1844366782 )
      
    
    rule  ( selector ( "myBytes()" ) => 1898923522 )
      
    
    rule  ( selector ( "myInt104()" ) => 3769717327 )
      
    
    rule  ( selector ( "myInt112()" ) => 1361874479 )
      
    
    rule  ( selector ( "myInt120()" ) => 2449055983 )
      
    
    rule  ( selector ( "myInt128()" ) => 1171335287 )
      
    
    rule  ( selector ( "myInt136()" ) => 1921575036 )
      
    
    rule  ( selector ( "myInt144()" ) => 3031097123 )
      
    
    rule  ( selector ( "myInt152()" ) => 2183556540 )
      
    
    rule  ( selector ( "myInt16()" ) => 1716680015 )
      
    
    rule  ( selector ( "myInt160()" ) => 2880209597 )
      
    
    rule  ( selector ( "myInt168()" ) => 64341664 )
      
    
    rule  ( selector ( "myInt176()" ) => 2473962370 )
      
    
    rule  ( selector ( "myInt184()" ) => 933893415 )
      
    
    rule  ( selector ( "myInt192()" ) => 3902309668 )
      
    
    rule  ( selector ( "myInt200()" ) => 2002425666 )
      
    
    rule  ( selector ( "myInt208()" ) => 103289144 )
      
    
    rule  ( selector ( "myInt216()" ) => 4128675402 )
      
    
    rule  ( selector ( "myInt224()" ) => 1054187961 )
      
    
    rule  ( selector ( "myInt232()" ) => 1299236373 )
      
    
    rule  ( selector ( "myInt24()" ) => 180311096 )
      
    
    rule  ( selector ( "myInt240()" ) => 193999351 )
      
    
    rule  ( selector ( "myInt248()" ) => 1172761411 )
      
    
    rule  ( selector ( "myInt256()" ) => 930181817 )
      
    
    rule  ( selector ( "myInt32()" ) => 652237467 )
      
    
    rule  ( selector ( "myInt40()" ) => 2688242429 )
      
    
    rule  ( selector ( "myInt48()" ) => 294352996 )
      
    
    rule  ( selector ( "myInt56()" ) => 1426573562 )
      
    
    rule  ( selector ( "myInt64()" ) => 1826080093 )
      
    
    rule  ( selector ( "myInt72()" ) => 1358599558 )
      
    
    rule  ( selector ( "myInt8()" ) => 1855112094 )
      
    
    rule  ( selector ( "myInt80()" ) => 2607424367 )
      
    
    rule  ( selector ( "myInt88()" ) => 4237602313 )
      
    
    rule  ( selector ( "myInt96()" ) => 1140454608 )
      
    
    rule  ( selector ( "myString()" ) => 1227618840 )
      
    
    rule  ( selector ( "myUint104()" ) => 2562905582 )
      
    
    rule  ( selector ( "myUint112()" ) => 2312572821 )
      
    
    rule  ( selector ( "myUint120()" ) => 3068336510 )
      
    
    rule  ( selector ( "myUint128()" ) => 2127339145 )
      
    
    rule  ( selector ( "myUint136()" ) => 4173203025 )
      
    
    rule  ( selector ( "myUint144()" ) => 4035797251 )
      
    
    rule  ( selector ( "myUint152()" ) => 360190854 )
      
    
    rule  ( selector ( "myUint16()" ) => 2385363659 )
      
    
    rule  ( selector ( "myUint160()" ) => 1383333939 )
      
    
    rule  ( selector ( "myUint168()" ) => 1009580974 )
      
    
    rule  ( selector ( "myUint176()" ) => 2404840593 )
      
    
    rule  ( selector ( "myUint184()" ) => 407000813 )
      
    
    rule  ( selector ( "myUint192()" ) => 229692326 )
      
    
    rule  ( selector ( "myUint200()" ) => 161744886 )
      
    
    rule  ( selector ( "myUint208()" ) => 3633238487 )
      
    
    rule  ( selector ( "myUint216()" ) => 3288289344 )
      
    
    rule  ( selector ( "myUint224()" ) => 1934302803 )
      
    
    rule  ( selector ( "myUint232()" ) => 2569544816 )
      
    
    rule  ( selector ( "myUint24()" ) => 946970341 )
      
    
    rule  ( selector ( "myUint240()" ) => 2223697895 )
      
    
    rule  ( selector ( "myUint248()" ) => 1057386179 )
      
    
    rule  ( selector ( "myUint256()" ) => 2816200220 )
      
    
    rule  ( selector ( "myUint32()" ) => 302881183 )
      
    
    rule  ( selector ( "myUint40()" ) => 2133099158 )
      
    
    rule  ( selector ( "myUint48()" ) => 2035097050 )
      
    
    rule  ( selector ( "myUint56()" ) => 3099541938 )
      
    
    rule  ( selector ( "myUint64()" ) => 1056558741 )
      
    
    rule  ( selector ( "myUint72()" ) => 329837525 )
      
    
    rule  ( selector ( "myUint8()" ) => 3802444463 )
      
    
    rule  ( selector ( "myUint80()" ) => 2279010072 )
      
    
    rule  ( selector ( "myUint88()" ) => 101404465 )
      
    
    rule  ( selector ( "myUint96()" ) => 2823172538 )
      
    
    rule  ( selector ( "setMyBool(bool)" ) => 3944427737 )
      

endmodule

module STORAGE-VERIFICATION
    imports public Storage-CONTRACT
    
    

endmodule

