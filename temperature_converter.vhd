--Pictures of xilinx the board will be sent by email
--circuit converts 4-bit user temperature input and converts it to kelvin and fahrenheit
--and allows selection between displaying kelvin, fahrenheit, and celcius


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;


entity midterm_proj is
    Port ( af : in STD_LOGIC_VECTOR (3 downto 0); --user input bits in celcius
           sel : in STD_LOGIC; --selects between fahrenheit and kelvin to displa
           celc : in STD_LOGIC; --displays celcius if 1
           clk : in STD_LOGIC; 
           outf : out STD_LOGIC_VECTOR (3 downto 0); --output bits
           cel : out STD_LOGIC; --indicates if temperature is in celcius
           far : out STD_LOGIC; --indicates if temperature is in fahrenheit
           kel : out STD_LOGIC); --indicates if temperature is in kelvin
         
end midterm_proj;

architecture Behavioral of midterm_proj is

--1x2 decoder
component decode_1x2
port (IN0 : in std_logic;
      D1, D0: out std_logic);
end component; 

--2x1mux (selector)
component mux_2x1 
port (a, b, sel : in std_logic;
     y : out std_logic);
end component;

--adds 5 to kelvin as per project specification using a ripple-carry adder
component c_to_k
port (cf: in std_logic_vector;
      SUMf : out std_logic_vector);
end component; 

--stores user input
component fbit_register
port (D : in std_logic_vector;
      clk : in std_logic;
      Q : out std_logic_vector);
end component;

--multiplies input by 7/6 and adds 1 as per project specification
component c_to_f
port (a : in std_logic_vector;
      y : out std_logic_vector); 
end component;

signal s0, s1, s2, c2f0, c2f1, c2f2, c2f3, c2k0, c2k1, c2k2, c2k3, r0, r1, r2, r3 : std_logic; 
begin 

dec1 : decode_1x2 port map(IN0 => sel, D0=> s1, D1 => s0); 
mux1 : mux_2x1 port map(a => s0, b => s1, sel => '0', y => s2); 
reg1 : fbit_register port map(clk => clk, D(3) => af(0), D(2) => af(1), D(1) => af(2), D(0) => af(3), Q(0) => r0, Q(1) => r1, Q(2) => r2, Q(3) => r3);
K : c_to_k port map(cf(0) => af(3), cf(1) => af(2), cf(2) => af(1), cf(3) => af(0), SUMf(0) => c2k3, SUMf(1) => c2k2, SUMf(2) => c2k1, SUMf(3) => c2k0);
F : c_to_f port map(a(0) => af(0), a(1) => af(1), a(2) => af(2), a(3) => af(3), y(0) => c2f3, y(1) => c2f2, y(2) => c2f1, y(3) => c2f0);

process (clk)
begin
--outputs celcius temperature if celc is 1
if (celc = '1') then 
outf(0) <= af(0);
outf(1) <= af(1);
outf(2) <= af(2);
outf(3) <= af(3);
cel <= '1';
far <= '0';
kel <= '0';
--outputs kelvin temperature if sel is 0
elsif (s2 = '0') then 
outf(0) <= c2k0;
outf(1) <= c2k1;
outf(2) <= c2k2;
outf(3) <= c2k3;
cel <= '0';
far <= '0';
kel <= '1';
--outputs fahrenheit temperature if sel is 1
elsif (s2 = '1')then 
outf(0) <= c2f3; 
outf(1) <= c2f2;
outf(2) <= c2f1;
outf(3) <= c2f0;
cel <= '0';
far <= '1';
kel <= '0';
--if unknown, output celcius
else
outf(0) <= af(0);
outf(1) <= af(1);
outf(2) <= af(2);
outf(3) <= af(3);

end if;
end process;


end Behavioral;


