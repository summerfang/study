
public class DataType {
	public static void main(String[] argv){
		// Integer
		byte b_smallest = -128;
		byte b_biggest = 127;

		short sh_smallest = -32768;
		short sh_largest = 32767;

		int i_smallest = -2147483648;
		int i_largest = 2147483647;

		long l_smallest = -9223372036854775808L;
		long l_largest = 9223372036854775807L;

		char c_smallest = 0;
		char c_largest = 65535;

		// Float
		float f = 0.123456f;

		// Double
		double d = 0.1234567890123d;

		// Boolean
		boolean b = true;
		
		// String
		String str = "Hello World!";
		System.out.print(str);

	}
}