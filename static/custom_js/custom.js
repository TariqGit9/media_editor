
function getRandomDarkColor() {
    // Generate random values for red, green, and blue components
    var r = Math.floor(Math.random() * 128); // Keep it in the lower half of the color spectrum
    var g = Math.floor(Math.random() * 128);
    var b = Math.floor(Math.random() * 128);
  
    // Convert the RGB values to a hex color code
    var hexColor = "#" + r.toString(16).padStart(2, '0') + g.toString(16).padStart(2, '0') + b.toString(16).padStart(2, '0');

    return hexColor;
}
