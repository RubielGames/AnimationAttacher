bl_info = {
    "name": "Animation Attacher",
    "author": "Rubiel",
    "version": (1, 0),
    "blender": (3, 4, 0),
    "location": "View3D > Sidebar > Animation Attacher",
    "description": "Attach an animation to an object",
    "category": "Animation",
}

import bpy


class AnimationAttacher(bpy.types.Operator):
    bl_idname = "anim.attach"
    bl_label = "Attach Animation"
    bl_description = "Attach an animation to the selected character"

    def execute(self, context):
        props = context.scene.animation_attacher_props

        character_obj = bpy.data.objects.get(props.character_name)
        new_animation_root_obj = bpy.data.objects.get(props.new_animation_root_name)

        if character_obj is None:
            self.report({'ERROR'}, "Character not found.")
            return {'CANCELLED'}
        if new_animation_root_obj is None:
            self.report({'ERROR'}, "New animation root node not found.")
            return {'CANCELLED'}
        else:
            new_animation_action = new_animation_root_obj.animation_data.action

            if new_animation_action is not None:
                bpy.context.view_layer.objects.active = character_obj
                bpy.ops.object.select_all(action='DESELECT')
                character_obj.select_set(True)
                bpy.context.view_layer.objects.active = new_animation_root_obj
                bpy.ops.object.parent_set(type='ARMATURE')

                character_obj.animation_data_create()
                track = character_obj.animation_data.nla_tracks.new()
                track.name = props.nla_track_name
                strip = track.strips.new(name=new_animation_action.name, start=0, action=new_animation_action)

                strip.blend_type = 'REPLACE'
                strip.influence = 1.0

                if props.remove_root_movement:
                    for fcu in new_animation_root_obj.animation_data.action.fcurves:
                        if fcu.data_path == "location" and fcu.array_index == 1:
                            fcu.mute = True

                new_animation_root_obj.hide_set(True)
                bpy.context.collection.objects.unlink(new_animation_root_obj)
                bpy.data.objects.remove(new_animation_root_obj)
            else:
                self.report({'ERROR'}, "New animation action not found in the new animation root node.")
                return {'CANCELLED'}
        return {'FINISHED'}


class AnimationAttacherSyncNames(bpy.types.Operator):
    bl_idname = "anim.sync_names"
    bl_label = "Sync Names"
    bl_description = "Sync animation name to NLA track name"

    def execute(self, context):
        props = context.scene.animation_attacher_props
        props.nla_track_name = props.new_animation_root_name
        return {'FINISHED'}


class AnimationAttacherPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Animation Attacher'
    bl_label = 'Animation Attacher'

    def draw(self, context):
        layout = self.layout
        props = context.scene.animation_attacher_props

        layout.prop(props, "character_name")
        
        row = layout.row()
        row.prop(props, "new_animation_root_name")
        row.operator('anim.sync_names', text="", icon='FILE_REFRESH')
        
        layout.prop(props, "nla_track_name")
        layout.prop(props, "remove_root_movement")

        layout.operator("anim.attach")


class AnimationAttacherProperties(bpy.types.PropertyGroup):
    character_name: bpy.props.StringProperty(
        name="Object to animate",
        description="Name of the object you want your animation to be attached to",
        default="Root"
    )

    new_animation_root_name: bpy.props.StringProperty(
        name="Animation",
        description="Name of the root of animation object",
        default="Root.001"
    )

    nla_track_name: bpy.props.StringProperty(
        name="NLA Track",
        description="Name of the NLA track",
        default="Root.001"
    )

    remove_root_movement: bpy.props.BoolProperty(
        name="Remove root movement",
        description="Mutes Y location keyframes of selected armature",
        default=False
    )


def register():
    bpy.utils.register_class(AnimationAttacherProperties)
    bpy.types.Scene.animation_attacher_props = bpy.props.PointerProperty(type=AnimationAttacherProperties)
    bpy.utils.register_class(AnimationAttacher)
    bpy.utils.register_class(AnimationAttacherSyncNames)
    bpy.utils.register_class(AnimationAttacherPanel)


def unregister():
    bpy.utils.unregister_class(AnimationAttacher)
    bpy.utils.unregister_class(AnimationAttacherSyncNames)
    bpy.utils.unregister_class(AnimationAttacherPanel)
    del bpy.types.Scene.animation_attacher_props
    bpy.utils.unregister_class(AnimationAttacherProperties)


if __name__ == "__main__":
    register()
