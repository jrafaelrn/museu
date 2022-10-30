require('log-timestamp');

import Upscaler from 'upscaler';
const upscaler = new Upscaler();

upscaler.upscale('/temp/0.png', {
    scale: 4,
    progress: (progress) => {
        console.log(`Progress: ${progress}%`);
    }

    }).then(upscaledImage => {
        
        // upscaledImage is a buffer containing the upscaled image
        // you can save it to a file or do whatever you want with it
        fs.writeFileSync('/temp/0-upscaler.png', upscaledImage);

    }
)