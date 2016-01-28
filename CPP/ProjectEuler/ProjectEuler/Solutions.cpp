//
//  Solutions.cpp
//  ProjectEuler
//
//  Created by Jeff Hajewski on 1/28/16.
//  Copyright © 2016 j-haj. All rights reserved.
//

#include "Solutions.hpp"
#include <vector>

int Solutions::pe1(int a, int b, int n) {
    auto sum(0);
    for (int i = 0; i < n; ++i) {
        if ((i % a == 0) && (i % b == 0)) {
            sum += i;
        } else if (i % a == 0) {
            sum += i;
        } else if (i % b == 0) {
            sum += i;
        }
    }
    return sum;
}