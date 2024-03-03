def simply_supported_uniformload(length, load):
    return (load * (length**2))/8

def cantilever_uniformload(length, load):
    return (load * (length**2))/2

def fixed_and_support_uniformload(length, load):
    return (load * (length**2))/8

def overhang_support_uniformload(length, load):
    return()

def fixed_ended_uniformload(length, load):
    return (load * (length**2))/12

def continous_twoequalspan_uniformload(length, load1, load2):
    return()

def continous_twounequalspan_uniformload(length1, legth2, load1, load2):
    return()

print(simply_Supported_uniformload(1,5))