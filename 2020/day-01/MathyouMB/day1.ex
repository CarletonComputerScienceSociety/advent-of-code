{:ok, contents} = File.read("problem1.txt")
formatted_contents = contents |> String.split("\n", trim: true) |> Enum.map(fn n -> Integer.parse(n) |> elem(0) end)
Enum.each(formatted_contents, fn i -> Enum.each(formatted_contents, fn j -> if i+j == 2020 do IO.puts i*j end end) end)