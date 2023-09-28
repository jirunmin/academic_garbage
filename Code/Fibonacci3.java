public class Fibonacci3 {
    static int fibonacci3(int a){
        if(1<a) return fibonacci3(-2+a) + fibonacci3(-1+a);
        else    return a;
    }
}
