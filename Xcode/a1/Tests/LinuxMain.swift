import XCTest

import a1Tests

var tests = [XCTestCaseEntry]()
tests += a1Tests.allTests()
XCTMain(tests)