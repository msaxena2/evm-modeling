// SPDX-License-Identifier: UNLICENSED
pragma solidity =0.8.13;

import "forge-std/Test.sol";
import "src/Prank.sol";

contract AdditionalToken {
    address public immutable owner;
    uint256 public count;

    constructor() {
        owner = msg.sender;
        count = 0;
    }

    function incrementCount() public {
        require(msg.sender != owner);
        count = count + 1;
    }
}

contract PlainPrankTest is Test {

    function test_startPrank_true() public {
        AdditionalToken token = new AdditionalToken();
        vm.startPrank(address(token));
        token.incrementCount();
        vm.stopPrank();
        assert(token.count() == 1);
    }

    // function test_startPrankWithOrigin_true() public {
    //     AdditionalToken token = new AdditionalToken();
    //     vm.startPrank(address(token), address(token));
    //     token.incrementCount();
    //     vm.stopPrank();
    //     assert(token.count() == 1);
    // }

    // function test_stopPrank_true() public {
    //     vm.stopPrank();
    //     vm.stopPrank();
    // }

    // function test_stopPrank_true2() public {
    //     AdditionalToken token = new AdditionalToken();
    //     vm.startPrank(address(token));
    //     token.incrementCount();
    //     assert(token.count() == 1);
    // }

    // function test_zeroPrank_true() public {
    //     AdditionalToken token = new AdditionalToken();
    //     vm.startPrank(address(0));
    //     token.incrementCount();
    //     vm.stopPrank();
    //     assert(token.count() == 1);
    // }

}