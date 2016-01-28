//
//  main.cpp
//  ProjectEulerTests
//
//  Created by Jeff Hajewski on 1/28/16.
//  Copyright © 2016 j-haj. All rights reserved.
//

#include <iostream>
#include <gtest/gtest.h>

TEST(SomeTest, test) {
    EXPECT_EQ(1, 1);
}

int main(int argc, char * argv[]) {
    // insert code here...
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
