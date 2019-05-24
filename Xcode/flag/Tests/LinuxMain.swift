import XCTest

import flagTests

var tests = [XCTestCaseEntry]()
tests += flagTests.allTests()
XCTMain(tests)