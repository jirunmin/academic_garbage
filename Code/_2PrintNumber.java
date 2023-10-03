import java.util.Arrays;
import java.util.Scanner;

public class _2PrintNumber {
    public static void PrintNum(int i, int j, int k)
    {
        int x = i;
        L1:while(x <= j)
        {
            for(int a=0; a<k; a++)
            {
                if(x > j)   break L1;
                System.out.print(x + " ");
                x++;
            }
            System.out.println("");
        }
    }
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int i = scanner.nextInt();
        int j = scanner.nextInt();
        int k = scanner.nextInt();

        PrintNum(i, j, k);
    }
}
