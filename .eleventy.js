module.exports = function(eleventyConfig) {
  // CSS, JS, Bilder kopieren
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("data/player_images");

  // CSV zu JSON Filter
  eleventyConfig.addFilter("fromCSV", function(csvString) {
    const lines = csvString.split('\n');
    const headers = lines[0].split(',').map(h => h.trim());
    return lines.slice(1).filter(line => line.trim()).map(line => {
      const values = line.split(',');
      let obj = {};
      headers.forEach((header, i) => {
        obj[header] = values[i] ? values[i].trim() : '';
      });
      return obj;
    });
  });

  // Datum Formatierung
  eleventyConfig.addFilter("formatDate", function(date) {
    return new Date(date).toLocaleDateString('de-AT', {
      day: '2-digit',
      month: 'long',
      year: 'numeric'
    });
  });

  // Limit Filter für Arrays
  eleventyConfig.addFilter("limit", function(array, limit) {
    return array.slice(0, limit);
  });

  return {
    dir: {
      input: "src",
      output: "dist",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "md", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk"
  };
};
