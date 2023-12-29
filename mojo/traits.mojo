

fn main():
    use_trait_function()

trait cry:
    fn required_method(self, x: Int): ...

struct Man(cry):
    fn __init__(inout self):
        pass

    fn required_method(self, x: Int): 
        print("hello traits")


fn fun_with_traits[T: cry](x: T):
    x.required_method(42)

fn use_trait_function():
    let thing = Man()
    fun_with_traits(thing)