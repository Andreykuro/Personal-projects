def separating_axis_theorem(object1, object2):
    # Define axes to test for separation
    axes = [object1.normal] + object2.normals
    for axis in axes:
        # Project both objects onto the axis
        proj1 = project_onto_axis(object1, axis)
        proj2 = project_onto_axis(object2, axis)
        # Check if projections overlap
        if not do_intervals_overlap(proj1, proj2):
            return False # Separating axis found, objects are not colliding
    return True # No separating axis found, objects are colliding