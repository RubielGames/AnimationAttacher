# Animation Attacher Addon for Blender

## Description

The Animation Attacher addon for Blender provides a convenient way to attach an animation to a character. This addon features a side panel where you can select a character and an animation, specify the name of the Nonlinear Animation (NLA) track, and opt to remove root movement by resetting Y location keyframes.

## Installation
Follow these steps to install the addon:
1. Click on the green "Code" button on this GitHub page and select "Download ZIP".
2. Save the ZIP file to your computer.
3. Open Blender.
4. Navigate to `Edit > Preferences`.
5. Click on the "Add-ons" tab.
6. Click on the "Install..." button at the top of the Preferences window.
7. Find the saved ZIP file in your files and click "Install Add-on".
8. The addon should now appear in the list of add-ons. Enable it by checking the box next to the addon's name.

## Usage
To use the Animation Attacher addon:
1. Go to the 3D Viewport.
2. Open the sidebar by pressing `N` or clicking on the small arrow at the top right of the 3D Viewport.
3. Find and click on the new tab titled "Animation Attacher" to open the addon's panel.
4. The panel contains text fields for entering the names of the character and animation, as well as a field for specifying the name of the NLA track. The name of the NLA track defaults to the name of the animation.
5. To remove root movement from the animation, check the "Remove root movement" box. This could be useful if you're using an animation exported from Mixamo, for instance. Keep in mind that this is a "destructive" operation as one axis of keyframes will be removed. This isn't necessary if your game engine removes root movement.
6. After entering all the necessary information, click the "Attach Animation" button. This attaches the specified animation to the chosen character. You can also `drag and drop` names from the Outliner into the Animation Attacher fields.

## Example Workflow
1. Start with your model in FBX.
2. Upload it to Mixamo using `Upload Character`.
3. Attach a Mixamo animation.
4. Once you're satisfied with the animation, click "Download".
   * Choose `FBX binary`, `Without skin`, `60 frames`, and `none` for keyframe reduction.
   * Click "Download".
5. In Blender, import the FBX character you used in Mixamo - it will be called `Root` if it was an empty project.
6. Import the animation you downloaded from Mixamo - it will be named `Root.001` if it's the first animation.
7. Attach the animation:
   * Drag and drop `Root` from the Outliner into the `Object` field.
   * Drag and drop `Root.001` from the Outliner into the `Animation` field.
   * Name the animation in the NLA name field - for example, if you exported a running animation, call it "Run fast".
   * If you are using a Mixamo running/walking animation that includes root movement, but you want to control movement in your game engine, check `Remove root movement` to get the animation in place.
   * Click `Attach Animation`.
8. Open a new editor, the `Nonlinear Animation`, and you should see a new line there called "Run fast".
   * Click the star to the left of the name.
   * Press `space` to play the animation.
