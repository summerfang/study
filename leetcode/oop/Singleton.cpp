#include <iostream>

class Singleton {
    private:
    static Singleton* _instance;

    // Private constructor to prevent instantiation
    Singleton() {
        value = 42;
    }

    public:
    static Singleton* getInstance() {
        if (_instance == nullptr) {
            _instance = new Singleton();
        }
        return _instance;
    }

    int getValue() const {
        return value;
    }

    private:
    int value;
};

Singleton* Singleton::_instance = nullptr;

int main() {
    Singleton* singleton1 = Singleton::getInstance();
    Singleton* singleton2 = Singleton::getInstance();

    std::cout << (singleton1 == singleton2) << std::endl;  // true
    std::cout << singleton1->getValue() << std::endl;      // 42

    return 0;
}
