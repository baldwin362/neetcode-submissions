class Singleton {
private: 
    string val; 
    Singleton() {}

public:

    static Singleton *getInstance() {
        static Singleton* unique_instance = new Singleton(); ///static means that this is created and stays the same for all instances of this class
        /// when calling static in modern C++ we call the constructor Singleton() automatically 
        return unique_instance; 
    }

    string getValue() {
        return val; 
    }

    void setValue(string &value) {
        val = value; 
    }


};
