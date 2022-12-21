package main

import "testing"

func TestSum(t *testing.T) {
  if dividenum(5,1) != 5 {
    t.Fail()
  }
  if dividenum(5,2) != 2 {
    t.Fail()
  }
  if dividenum(6,3) != 2 {
    t.Fail()
  }
}
