public class Fibonacci4 {
    static int fibonacci4(int a){
        return (1<a)?fibonacci4(-2+a)+fibonacci4(-1+a):a;
    }
}
