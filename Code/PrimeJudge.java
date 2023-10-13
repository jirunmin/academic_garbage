import java.util.Scanner;

public class PrimeJudge {
    public static boolean isPrime(int x)
    {
        if(x < 2)   return false;

        for(int i=2; i<=x/i; i++)
            if(x % i == 0)
                return false;

        return true;
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入一个正整数值：");
        int n = scanner.nextInt();

        if(isPrime(n))
            System.out.println("是质数");
        else
            System.out.println("不是质数");
    }
}
