const std = @import("std");

const Allocator = std.mem.Allocator;
const Reader = std.io.Reader;
const ArrayList = std.ArrayList;

const stdout = std.io.getStdOut().writer();

// Loads file and splits lines.
pub fn readData(alloc: Allocator, file_path: []const u8) anyerror!ArrayList([]u8) {
    var res = ArrayList([]u8).init(alloc);

    // Open the file
    var file = try std.fs.cwd().openFile(file_path, .{ .read = true });
    defer file.close();

    // Read the contents
    const buffer_size: u64 = 4096;
    const file_buffer = try file.readToEndAlloc(alloc, buffer_size);
    defer alloc.free(file_buffer);

    // Break up the file into lines
    var iter: std.mem.SplitIterator(u8) = std.mem.split(u8, file_buffer, "\n");
    while (iter.next()) |line| {
        if (std.mem.eql(u8, line, "")) {
            continue;
        }
        var temp = try alloc.alloc(u8, line.len);
        std.mem.copy(u8, temp, line);
        try res.append(temp);
    }

    return res;
}

pub fn cleanup(allocator: Allocator, list: ArrayList([]u8)) void {
    var items = list.items;
    for (items) |val| {
        allocator.free(val);
    }
    list.deinit();
}

pub fn part1(input: []u8) anyerror!u64 {
    var i: usize = 3;
    mainloop: while (i < input.len) : (i += 1) {
        var a = i - 3;
        while (a < i) : (a += 1) {
            var b = a + 1;
            while (b <= i) : (b += 1) {
                if (input[a] == input[b]) {
                    continue :mainloop;
                }
            }
        }
        try stdout.print("Part1 str = {s}\n", .{input[i - 3 .. i + 1]});
        return i + 1;
    }
    return input.len;
}

pub fn part2(input: []u8) anyerror!u64 {
    var i: usize = 13;
    mainloop: while (i < input.len) : (i += 1) {
        var a = i - 13;
        while (a < i) : (a += 1) {
            var b = a + 1;
            while (b <= i) : (b += 1) {
                if (input[a] == input[b]) {
                    continue :mainloop;
                }
            }
        }
        try stdout.print("Part2 Str = {s}\n", .{input[i - 13 .. i + 1]});
        return i + 1;
    }
    return input.len;
}

test "Days" {
    const allocator = std.testing.allocator;

    var data = try readData(allocator, "input");
    var string = data.pop();
    defer cleanup(allocator, data);
    defer allocator.free(string);

    var p1 = part1(string);
    var p2 = part2(string);

    try stdout.print("Part1 = {}\n", .{p1});
    try stdout.print("Part2 = {}\n", .{p2});
}
