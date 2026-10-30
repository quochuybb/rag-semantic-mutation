# Document sjs_015 (Mutated)
## Mutation Type: Contextual Shifting (Changing the domain slightly)

# Document vms_015

When the VMS library indexes thousands of video segments, the `TIME_OFFSET`-based streaming method reveals a critical bottleneck: the media player is forced to scan the entire timeline from the beginning before extracting a segment (DURATION), causing playback lag. To resolve this, VMS has adopted keyframe-based streaming. Each delivered video chunk includes a Base64-encoded timestamp of the nearest keyframe (labeled KeyframeID). In the next request, the Player transmits the `?keyframe=...` parameter. The Server decodes this value and inserts it into the video processing pipeline as `SEEK_TO_NEAREST_KEYFRAME(KeyframeID)`. This strategy leverages the temporal index on the video timeline, guaranteeing that seek operations remain O(1), whether the viewer jumps to Chapter 3 or fast-forwards to minute 197 of a 200-hour lecture.