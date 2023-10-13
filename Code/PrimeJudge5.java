import java.util.Scanner;

public class PrimeJudge5 {
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
    public static boolean isPrime(int x)
    {
        if(x < 2)   return false;
        if(x == 2)  return true;

        int i = 2;

        while(i <= x/i)
        {
            if(x % i == 0)
                return false;
            i++;
        }

        return true;
    }
}
