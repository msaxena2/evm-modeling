// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import "forge-std/Test.sol";
import "ds-math/math.sol";

contract LoopsTest is Test, DSMath {
    function setUp() public {}

    function sumToN(uint256 n) internal pure returns (uint256) {
        uint256 result = 0;
        for (uint256 i = 0; i <= n; i++) {
            result += i;
        }
        return result;
    }

    function sumToNBroken(uint256 n) internal pure returns (uint256) {
        uint256 result = 0;
        // Off by one error in loop condition
        for (uint256 i = 0; i < n; i++) {
            result += i;
        }
        return result;
    }

    function testSumToN(uint256 n) public {
        vm.assume(n <= 100); // We need this to keep the test running time low
        uint256 expected = n * (n + 1) / 2;
        uint256 actual = sumToN(n);
        assertEq(expected, actual);
    }

    function testSumToNBroken(uint256 n) public {
        // This test should fail
        vm.assume(n <= 100); // We need this to keep the test running time low
        uint256 expected = n * (n + 1) / 2;
        uint256 actual = sumToNBroken(n);
        assertEq(expected, actual);
    }
    
    function max(uint256[] memory numbers) internal pure returns (uint256) {
        uint256 result = 0;
        for (uint256 i = 0; i < numbers.length; i++) {
            if (numbers[i] > result) result = numbers[i];
        }
        return result;
    }

    function maxBroken(uint256[] memory numbers) internal pure returns (uint256) {
        uint256 result = 0;
        // Off by one error in loop initialization
        for (uint256 i = 1; i < numbers.length; i++) {
            if (numbers[i] > result) result = numbers[i];
        }
        return result;
    }

    function testMax(uint256[] memory numbers) public {
        uint256 maxium = max(numbers);
        bool isMax = true;
        for (uint256 i = 0; i < numbers.length && isMax; i++) {
            isMax = maxium >= numbers[i];
        }
        assertTrue(isMax);
    }

    function testMaxBroken(uint256[] memory numbers) public {
        // This test should fail
        uint256 maxium = maxBroken(numbers);
        bool isMax = true;
        for (uint256 i = 0; i < numbers.length && isMax; i++) {
            isMax = maxium >= numbers[i];
        }
        assertTrue(isMax);
    }

    function sort(uint256[] memory numbers) internal pure returns(uint256[] memory) {
        if (numbers.length <= 1) return numbers;
        quickSort(numbers, 0, numbers.length - 1);
        return numbers;
    }

    function sortBroken(uint256[] memory numbers) internal pure returns(uint256[] memory) {
        if (numbers.length <= 1) return numbers;
        // Off by one error in second parameter
        quickSort(numbers, 1, numbers.length - 1);
        return numbers;
    }

    function quickSort(uint[] memory numbers, uint left, uint right) internal pure {
        if (left >= right) return;
        uint i = left;
        uint j = right;
        uint pivot = numbers[left + (right - left) / 2];
        while (i <= j) {
            while (numbers[i] < pivot) i++;
            while (pivot < numbers[j] && j > 0) j--;
            if (i <= j) {
                (numbers[i], numbers[j]) = (numbers[j], numbers[i]);
                i++;
                if (j > 0) j--;
            }
        }
        if (left < j)
            quickSort(numbers, left, j);
        if (i < right)
            quickSort(numbers, i, right);
    }

    function testSort(uint256[] memory numbers) public {
        uint256[] memory sorted = sort(numbers);
        bool isSorted = true;
        for (uint256 i = 1; i < sorted.length && isSorted; i++) {
            isSorted = numbers[i - 1] <= numbers[i];
        }
        assertTrue(isSorted);
    }

    function testSortBroken(uint256[] memory numbers) public {
        // This test should fail
        uint256[] memory sorted = sortBroken(numbers);
        bool isSorted = true;
        for (uint256 i = 1; i < sorted.length && isSorted; i++) {
            isSorted = numbers[i - 1] <= numbers[i];
        }
        assertTrue(isSorted);
    }

    function sqrt(uint x) internal pure returns (uint y) {
        if (x == 0) {
            y = 0;
        } else {
            uint z = x;
            while (true) {
                y = z;
                z = add(wdiv(x, z), z) / 2;
                if (y == z) {
                    break;
                }
            }
        }
    }

    function testSqrt(uint x) public {
        uint res = sqrt(x);
        uint sqr = wmul(res, res);
        uint err;
        if (sqr > x) {
            err = sqr - x;
        } else {
            err = sqr - res;
        }
        assertTrue(err < x / 100);
    }
}
