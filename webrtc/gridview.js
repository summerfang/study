let participant_videos = document.getElementsByClassName('participant_video');

console.log(participant_videos.length)

participants = 0;

setInterval(()=>{
    participants++;
    if (participants > participant_videos.length)
        return;
    
    let new_video = participant_videos[participants - 1]
    if (new_video != null) {
        let local_video;

        navigator.mediaDevices.getUserMedia({ video: true }).then((media_stream) => {
            local_video = new_video.srcObject = media_stream;
        }).catch();
    }
}, 1000)