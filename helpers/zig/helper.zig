//! helper.zig
//!
//! A simple helper library for advent of code in zig.
//! Currently just file reader and cleanup functions, will extend as needed
//!
//! Note: This is done with zig 0.9.1, though I believe this should be compatible with
//! 0.10.0

const std = @import("std");

const Allocator = std.mem.Allocator;
const Reader = std.io.Reader;
const ArrayList = std.ArrayList;

// Loads file and splits lines.
//
// Note: For those new to manually memory managed languages, you'll need
// to free the contents of the arraylist and deinit it.
// I've bundled a cleanup function this does this for you.
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

test "read_data" {
    const allocator = std.testing.allocator;
    const expect = std.testing.expect;

    var data = try readData(allocator, "../testfile.txt");
    defer cleanup(allocator, data);
    var items = data.items;

    var i: u64 = 0;
    while (i < items.len) : (i += 1) {
        const s: []const u8 = try std.fmt.allocPrint(allocator, "{}", .{i});
        defer allocator.free(s);

        try expect(std.mem.eql(u8, s, items[i]));
    }
}
