import string
from fuzzingbook.Grammars import srange, Grammar

#spam Grammar(after normalization and multiplication to remove negative and float values)
SPAM: Grammar = {
    "<start>": ["<f0> <f1> <f2> <f3> <f4> <f5> <f6> <f7> <f8> <f9> <f10> <f11> <f12> <f13> <f14> <f15> <f16> <f17> <f18> <f19> <f20> <f21> <f22> <f23> <f24> <f25> <f26> <f27> <f28> <f29> <f30> <f31> <f32> <f33> <f34> <f35> <f36> <f37> <f38> <f39> <f40> <f41> <f42> <f43> <f44> <f45> <f46> <f47> <f48> <f49> <f50> <f51> <f52> <f53> <f54> <f55> <f56> <f57> <f58> <f59> <f60> <f61> <f62> <f63> <f64> <f65> <f66> <f67> <f68> <f69> <f70> <f71> <f72> <f73> <f74> <f75> <f76> <f77> <f78> <f79> <f80> <f81> <f82> <f83> <f84> <f85> <f86> <f87> <f88> <f89> <f90> <f91> <f92> <f93> <f94> <f95> <f96> <f97> <f98> <f99>"],
    "<f0>": ["0", "<onenine><maybe_digits>"],
    "<f1>": ["0", "<onenine><maybe_digits>"],
    "<f2>": ["0", "<onenine><maybe_digits>"],
    "<f3>": ["0", "<onenine><maybe_digits>"],
    "<f4>": ["0", "<onenine><maybe_digits>"],
    "<f5>": ["0", "<onenine><maybe_digits>"],
    "<f6>": ["0", "<onenine><maybe_digits>"],
    "<f7>": ["0", "<onenine><maybe_digits>"],
    "<f8>": ["0", "<onenine><maybe_digits>"],
    "<f9>": ["0", "<onenine><maybe_digits>"],
    "<f10>": ["0", "<onenine><maybe_digits>"],
    "<f11>": ["0", "<onenine><maybe_digits>"],
    "<f12>": ["0", "<onenine><maybe_digits>"],
    "<f13>": ["0", "<onenine><maybe_digits>"],
    "<f14>": ["0", "<onenine><maybe_digits>"],
    "<f15>": ["0", "<onenine><maybe_digits>"],
    "<f16>": ["0", "<onenine><maybe_digits>"],
    "<f17>": ["0", "<onenine><maybe_digits>"],
    "<f18>": ["0", "<onenine><maybe_digits>"],
    "<f19>": ["0", "<onenine><maybe_digits>"],
    "<f20>": ["0", "<onenine><maybe_digits>"],
    "<f21>": ["0", "<onenine><maybe_digits>"],
    "<f22>": ["0", "<onenine><maybe_digits>"],
    "<f23>": ["0", "<onenine><maybe_digits>"],
    "<f24>": ["0", "<onenine><maybe_digits>"],
    "<f25>": ["0", "<onenine><maybe_digits>"],
    "<f26>": ["0", "<onenine><maybe_digits>"],
    "<f27>": ["0", "<onenine><maybe_digits>"],
    "<f28>": ["0", "<onenine><maybe_digits>"],
    "<f29>": ["0", "<onenine><maybe_digits>"],
    "<f30>": ["0", "<onenine><maybe_digits>"],
    "<f31>": ["0", "<onenine><maybe_digits>"],
    "<f32>": ["0", "<onenine><maybe_digits>"],
    "<f33>": ["0", "<onenine><maybe_digits>"],
    "<f34>": ["0", "<onenine><maybe_digits>"],
    "<f35>": ["0", "<onenine><maybe_digits>"],
    "<f36>": ["0", "<onenine><maybe_digits>"],
    "<f37>": ["0", "<onenine><maybe_digits>"],
    "<f38>": ["0", "<onenine><maybe_digits>"],
    "<f39>": ["0", "<onenine><maybe_digits>"],
    "<f40>": ["0", "<onenine><maybe_digits>"],
    "<f41>": ["0", "<onenine><maybe_digits>"],
    "<f42>": ["0", "<onenine><maybe_digits>"],
    "<f43>": ["0", "<onenine><maybe_digits>"],
    "<f44>": ["0", "<onenine><maybe_digits>"],
    "<f45>": ["0", "<onenine><maybe_digits>"],
    "<f46>": ["0", "<onenine><maybe_digits>"],
    "<f47>": ["0", "<onenine><maybe_digits>"],
    "<f48>": ["0", "<onenine><maybe_digits>"],
    "<f49>": ["0", "<onenine><maybe_digits>"],
    "<f50>": ["0", "<onenine><maybe_digits>"],
    "<f51>": ["0", "<onenine><maybe_digits>"],
    "<f52>": ["0", "<onenine><maybe_digits>"],
    "<f53>": ["0", "<onenine><maybe_digits>"],
    "<f54>": ["0", "<onenine><maybe_digits>"],
    "<f55>": ["0", "<onenine><maybe_digits>"],
    "<f56>": ["0", "<onenine><maybe_digits>"],
    "<f57>": ["0", "<onenine><maybe_digits>"],
    "<f58>": ["0", "<onenine><maybe_digits>"],
    "<f59>": ["0", "<onenine><maybe_digits>"],
    "<f60>": ["0", "<onenine><maybe_digits>"],
    "<f61>": ["0", "<onenine><maybe_digits>"],
    "<f62>": ["0", "<onenine><maybe_digits>"],
    "<f63>": ["0", "<onenine><maybe_digits>"],
    "<f64>": ["0", "<onenine><maybe_digits>"],
    "<f65>": ["0", "<onenine><maybe_digits>"],
    "<f66>": ["0", "<onenine><maybe_digits>"],
    "<f67>": ["0", "<onenine><maybe_digits>"],
    "<f68>": ["0", "<onenine><maybe_digits>"],
    "<f69>": ["0", "<onenine><maybe_digits>"],
    "<f70>": ["0", "<onenine><maybe_digits>"],
    "<f71>": ["0", "<onenine><maybe_digits>"],
    "<f72>": ["0", "<onenine><maybe_digits>"],
    "<f73>": ["0", "<onenine><maybe_digits>"],
    "<f74>": ["0", "<onenine><maybe_digits>"],
    "<f75>": ["0", "<onenine><maybe_digits>"],
    "<f76>": ["0", "<onenine><maybe_digits>"],
    "<f77>": ["0", "<onenine><maybe_digits>"],
    "<f78>": ["0", "<onenine><maybe_digits>"],
    "<f79>": ["0", "<onenine><maybe_digits>"],
    "<f80>": ["0", "<onenine><maybe_digits>"],
    "<f81>": ["0", "<onenine><maybe_digits>"],
    "<f82>": ["0", "<onenine><maybe_digits>"],
    "<f83>": ["0", "<onenine><maybe_digits>"],
    "<f84>": ["0", "<onenine><maybe_digits>"],
    "<f85>": ["0", "<onenine><maybe_digits>"],
    "<f86>": ["0", "<onenine><maybe_digits>"],
    "<f87>": ["0", "<onenine><maybe_digits>"],
    "<f88>": ["0", "<onenine><maybe_digits>"],
    "<f89>": ["0", "<onenine><maybe_digits>"],
    "<f90>": ["0", "<onenine><maybe_digits>"],
    "<f91>": ["0", "<onenine><maybe_digits>"],
    "<f92>": ["0", "<onenine><maybe_digits>"],
    "<f93>": ["0", "<onenine><maybe_digits>"],
    "<f94>": ["0", "<onenine><maybe_digits>"],
    "<f95>": ["0", "<onenine><maybe_digits>"],
    "<f96>": ["0", "<onenine><maybe_digits>"],
    "<f97>": ["0", "<onenine><maybe_digits>"],
    "<f98>": ["0", "<onenine><maybe_digits>"],
    "<f99>": ["0", "<onenine><maybe_digits>"],
    "<onenine>": srange("123456789"),
    "<maybe_digits>": ["", "<digits>"],
    "<digits>": ["<digit>", "<digit><digits>"],
    "<digit>": list(string.digits)
}
