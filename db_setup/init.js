// Connect to the database
db = db.getSiblingDB("mydatabase"); // Change database name if needed

// Drop existing collections (if needed, for a fresh start)
db.users.drop();
db.songs.drop();

// Create Users Collection
db.createCollection("users");
const user1 = db.users.insertOne({ name: "Alice", password: "password123", email: "alice@example.com", songs: [] });
const user2 = db.users.insertOne({ name: "Bob", password: "securepass", email: "bob@example.com", songs: [] });

print("✅ Users inserted!");

// Create Songs Collection (Referencing Users)
db.createCollection("songs");
const song1 = db.songs.insertOne({
  name: "Song A",
  artist: "Artist 1",
  link: "http://example.com/a",
  image: "http://example.com/img1.jpg",
  createdBy: user1.insertedId, // Reference Alice
});
const song2 = db.songs.insertOne({
  name: "Song B",
  artist: "Artist 2",
  link: "http://example.com/b",
  image: "http://example.com/img2.jpg",
  createdBy: user2.insertedId, // Reference Bob
});
const song3 = db.songs.insertOne({
  name: "Song C",
  artist: "Artist 3",
  link: "http://example.com/c",
  image: "http://example.com/img3.jpg",
  createdBy: user1.insertedId, // Another song by Alice
});

print("✅ Songs inserted!");

// Update Users to include their song references
db.users.updateOne({ _id: user1.insertedId }, { $set: { songs: [song1.insertedId, song3.insertedId] } });
db.users.updateOne({ _id: user2.insertedId }, { $set: { songs: [song2.insertedId] } });

print("✅ Users updated with song references!");
print("🎉 Database initialization complete!");
