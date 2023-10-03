import java.util.Scanner;
public class _2_1AddNum {
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int sum = 1;

        System.out.print("1");
        for(int i=3; i<=n; i+=2) {
            System.out.print(" + " + i);
            sum += i;
        }

        System.out.println(" = " + sum);
    }
}
