var Crawler = require("crawler");

var c = new Crawler({
    maxConnections : 10,
    // This will be called for each crawled page
    callback : function (error, res, done) {
        if(error){
            console.log(error);
        }else{
            var $ = res.$;
            // $ is Cheerio by default
            //a lean implementation of core jQuery designed specifically for the server
			$('.content').each(function(index){
				if (index == 0){
					return true;
				} else if (index >= 6){
					return false;
				}
				console.log("Index: " + index + "\n");
				var l = $(this).text()
				console.log(l);
			})
        }
        done();
    }
});

// Queue just one URL, with default callback
c.queue('http://www.physicsgre.com/viewtopic.php?f=3&t=145205&sid=d4d68c1850eaf4cd4cd5efa800e942fa');


// Queue some HTML code directly without grabbing (mostly for tests)

var davai = () => {
	console.log('kappa');
}
