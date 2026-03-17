#!/usr/bin/env python3
"""
Generate SEO landing pages for every exercise and Shift mode.
Data sourced from ExerciseCatalogGenerated.swift and ShiftProtocol.swift.
Run: python3 generate_pages.py
"""

import os, html as h, glob

BASE = os.path.dirname(os.path.abspath(__file__))
VIDEO_DIR = os.path.join(BASE, "assets", "video")

# Check which videos exist
available_videos = set()
for f in glob.glob(os.path.join(VIDEO_DIR, "*.mp4")):
    available_videos.add(os.path.splitext(os.path.basename(f))[0])

# ─────────────────────────────────────────────
# EXERCISE DATA (from ExerciseCatalogGenerated.swift — COMPLETE)
# ─────────────────────────────────────────────

exercises = [
    # ═══ Baseline Mobility — Fixed Core (6) ═══
    {"id":"passive_hang","name":"Passive Hang","dose":70,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Heavy arms. Quiet neck.","cue_detail":"Let the shoulders slide up without gripping. Stop shrug-winning the hang. Get heavy. That's the whole exercise.",
     "easier_title":"Feet assist.","easier_detail":"Let toes help. Neck stays soft. No shoulder shrug battle.",
     "harder_title":"Strict hang. Breathe slow.","harder_detail":"No toe support. Stop before grip panic. Build time, not suffering.",
     "targets":"Spinal decompression, grip endurance, shoulder mobility",
     "why":"Counteracts hours of seated compression. Hanging under bodyweight creates traction through the spine, opens the shoulder capsule, and builds grip endurance — all passively. Research shows decompression benefits begin after 60 seconds of sustained hang.",
     "how":["Find a bar or ledge you can hang from with feet off the ground","Let your body go completely heavy — no shrugging, no gripping with the neck","Breathe normally and let gravity do the work","If grip fails, rest and resume — accumulated time counts"]},

    {"id":"cat_cow","name":"Cat-Cow","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Segment the spine.","cue_detail":"Inhale to extend, exhale to round. Seven slow cycles. Each one should feel a little more open than the last.",
     "easier_title":"Smaller range. Gentle.","easier_detail":"Move what moves easily. No forcing.",
     "harder_title":"Pause at end-range. 3 seconds.","harder_detail":"Hold the round. Hold the arch. Breathe into the hold.",
     "targets":"Spinal segmental flexion and extension, breath coordination",
     "why":"Cat-cow mobilises each segment of the spine individually. Most people move their spine as a single block — this exercise trains it to articulate. The breath linkage also activates the diaphragm and calms the nervous system.",
     "how":["Start on all fours — hands under shoulders, knees under hips","Inhale: drop your belly, lift your chest and tailbone (cow)","Exhale: round your spine, tuck your chin and pelvis (cat)","Move one vertebra at a time — don't rush between positions"]},

    {"id":"thoracic_rotations","name":"Lying Thoracic Rotations","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Rotate through the ribcage.","cue_detail":"Hips stay still. Follow your hand with your eyes. If the hips are moving, the rotation isn't coming from the thoracic.",
     "easier_title":"Seated rotation.","easier_detail":"Sit in a chair. Rotate upper body only. Hands on shoulders.",
     "harder_title":"Open-book from side-lying.","harder_detail":"Full rotation with a pause at end-range. Control the return.",
     "targets":"Thoracic spine rotation, desk worker deficit correction",
     "why":"The thoracic spine is designed to rotate — but sitting all day locks it up. Lost thoracic rotation forces the lower back and neck to compensate, leading to pain. Just 40 seconds of controlled rotation restores range that most desk workers lose by midday.",
     "how":["Lie on your side with knees stacked and bent to 90°","Extend your top arm and rotate your upper body open","Follow your hand with your eyes — the gaze drives rotation","Keep your hips completely still — if they move, reduce the range"]},

    {"id":"ninety_ninety_transitions","name":"90-90 Hip Transitions","dose":50,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Rotation, not stretch.","cue_detail":"Feel the femur roll. If it turns pinchy, reduce range. Discomfort is useful information. Pain is not.",
     "easier_title":"Hands assist.","easier_detail":"Use your hands on the floor. Smaller transitions.",
     "harder_title":"Hands-free transitions.","harder_detail":"Sit tall. Let the hips do all the work.",
     "targets":"Hip internal and external rotation",
     "why":"Hip rotation is the most commonly lost range in adults who sit. The 90-90 position isolates internal and external rotation without compensating through the spine. Transitioning between sides trains the rotational control that protects knees and lower back.",
     "how":["Sit with both knees bent at 90° — one leg in front, one behind","Transition both legs to the other side in a windshield-wiper motion","Focus on the rotation happening at the hip joint, not the knee","Use hands on the floor for support if balance is an issue"]},

    {"id":"deep_squat_hold","name":"Deep Squat Hold","dose":55,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Settle in.","cue_detail":"This is a resting position, not a workout. Breathe and be heavy. If your heels lift, widen the stance.",
     "easier_title":"Assisted squat.","easier_detail":"Hold a doorframe or chair. Heels elevated if needed.",
     "harder_title":"Unassisted. Extended hold.","harder_detail":"Build toward 2 minutes. Shift weight side to side.",
     "targets":"Full-body integration — ankles, knees, hips, spine",
     "why":"The deep squat is a resting position used by every human culture — until chairs replaced it. Holding this position restores ankle dorsiflexion, hip flexion, and spinal alignment simultaneously. 55 seconds is enough to signal the nervous system that this range is safe.",
     "how":["Stand with feet slightly wider than shoulder-width","Sink your hips down between your knees as low as you can","Keep your heels on the ground — widen your stance if they lift","Breathe normally and let your body settle into the position"]},

    {"id":"couch_stretch","name":"Couch Stretch","dose":55,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Tall torso.","cue_detail":"Glute lightly engaged. No lumbar arch. The sensation should be in the front of the hip, not the low back.",
     "easier_title":"Back foot lower. More upright.","easier_detail":"Less stretch, more control. Keep breathing.",
     "harder_title":"Back foot high. Squeeze glute.","harder_detail":"Deeper hip flexor stretch. Torso stays tall. No leaning.",
     "targets":"Hip flexor length, quad stretch, anterior pelvic tilt correction",
     "why":"Sitting shortens the hip flexors. Shortened hip flexors tilt your pelvis forward and compress your lower back. The couch stretch targets the rectus femoris and iliopsoas directly. Research (Bandy 1997) shows 30 seconds per side is the minimum effective stretch duration.",
     "how":["Kneel with your back foot against a wall or couch","Step your front foot forward into a lunge position","Keep your torso tall and glute lightly engaged","The stretch should be in the front of the hip — not the lower back"]},

    # ═══ Baseline Mobility — Tail: Spinal Flow ═══
    {"id":"spinal_wave","name":"Spinal Wave","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Ripple, don't rush.","cue_detail":"Start from the pelvis. Let each segment follow the one below it. If you hit a stiff spot, slow down and breathe into it.",
     "easier_title":"Smaller ripple.","easier_detail":"Just pelvis and lower back. Upper body stays still.",
     "harder_title":"Full-body wave. Standing.","harder_detail":"Start from ankles, ripple through to fingertips.",
     "targets":"Spinal segmental control, body wave coordination",
     "why":"The spinal wave trains your body to move the spine sequentially — one vertebra at a time. Most people can only move their spine as a rigid block. This builds the neuromuscular control needed for fluid, pain-free movement.",
     "how":["Start on all fours or standing","Initiate the wave from your pelvis","Let each spinal segment follow the one below it","If you hit a stiff spot, slow down — that's where the work is"]},

    {"id":"jefferson_curl","name":"Jefferson Curl","dose":50,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"One vertebra at a time.","cue_detail":"Exhale as you roll down. No bounce, no yank. Controlled sequencing only.",
     "easier_title":"Shorten the range.","easier_detail":"Stop above discomfort. Control the descent. No stretch chasing.",
     "harder_title":"Full range. Slow tempo.","harder_detail":"Touch toes if earned. Same control. No bounce.",
     "targets":"Posterior chain flexibility, spinal articulation under load",
     "why":"The Jefferson curl builds loaded flexibility through the entire posterior chain — hamstrings, glutes, and every segment of the spine. Unlike a static toe touch, it trains your nervous system to trust end-range positions under control.",
     "how":["Stand tall on a slight elevation if available","Tuck your chin and begin rolling down one vertebra at a time","Exhale as you descend — inhale as you return","The return journey is identical: sequential, controlled, slow"]},

    {"id":"single_leg_goodmorning","name":"Single-Leg Good Morning","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Hip folds. Spine stays long.","cue_detail":"Balance through mid-foot. Square hips, square shoulders. Fix your gaze on one point.",
     "easier_title":"Shallow hinge. Hand on wall.","easier_detail":"Short range with support. Feel the hamstring load, don't chase depth.",
     "harder_title":"Full depth. Arms overhead.","harder_detail":"Longer lever, more balance demand. Hips stay square.",
     "targets":"Hamstring length, single-leg balance, hip hinge pattern",
     "why":"Combines the hip hinge with single-leg balance — two fundamental movement patterns in one exercise. The balance demand forces stabiliser muscles to engage, making the hamstring work more functional than a passive stretch.",
     "how":["Stand on one leg with a slight knee bend","Hinge forward at the hip, keeping your spine long","Square hips and shoulders throughout","Fix your gaze on one point — that alone halves the wobble"]},

    # ═══ Baseline Mobility — Tail: Hip Opening ═══
    {"id":"active_pigeon_stretch","name":"Active Pigeon","dose":50,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Control in and out.","cue_detail":"Stay active. Don't dump into the joint. Push the shin into the floor slightly. That keeps the glute online.",
     "easier_title":"Shin less angled.","easier_detail":"Front shin closer to body. Less external rotation demand.",
     "harder_title":"Shin more perpendicular.","harder_detail":"Work toward shin parallel to mat edge. Stay active, don't collapse.",
     "targets":"Hip external rotation, glute activation, hip flexor stretch",
     "why":"The pigeon stretch opens the hip in external rotation — a range most people lose from sitting. The 'active' version keeps the muscles engaged rather than passively dumping into the joint, which builds usable range rather than borrowed flexibility.",
     "how":["From all fours, bring one shin forward across your body","Keep the back leg extended behind you","Stay active — push the front shin into the floor lightly","Don't collapse into the stretch — maintain muscle engagement"]},

    {"id":"horse_stance_squats","name":"Horse Stance Squats","dose":45,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Feet press out. Knees track.","cue_detail":"Even pressure across the foot. Don't collapse inward to find depth.",
     "easier_title":"Narrower stance. Shallower.","easier_detail":"Find a width you own. Don't chase wide.",
     "harder_title":"Wider. Longer holds at bottom.","harder_detail":"Sit deeper. Hold 5 seconds at the bottom of each rep.",
     "targets":"Hip adductors, inner thigh mobility, lateral hip strength",
     "why":"Wide-stance squatting loads the adductors and inner thigh — muscles that get chronically tight from sitting with knees together. The horse stance also builds lateral hip strength that protects the knees during everyday movement.",
     "how":["Stand with feet wide, toes slightly turned out","Sit down into a wide squat, pressing knees out over toes","Even pressure across the whole foot","Don't collapse inward to find depth — less depth with clean form beats more"]},

    # ═══ Baseline Mobility — Tail: Shoulder ═══
    {"id":"shoulder_extensions","name":"Behind-Back Shoulder Stretch","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Chest opens. Ribs stay down.","cue_detail":"Feel the front shoulder lengthen, not the low back arching. Ribs down.",
     "easier_title":"Hands wider.","easier_detail":"Less stretch, more control. Ribs stay down.",
     "harder_title":"Hands closer. Slow lift.","harder_detail":"Feel the front of the shoulder open. Hold the top.",
     "targets":"Anterior shoulder mobility, chest opening, posture correction",
     "why":"Desk work rounds the shoulders forward, shortening the front of the shoulder capsule. This stretch reverses that pattern by opening the anterior shoulder while keeping the ribs down — preventing the common compensation of arching the lower back.",
     "how":["Clasp your hands behind your back","Lift your arms away from your body","Keep your ribs down — the stretch should be in the front of the shoulder","If you feel it in your lower back, you're arching too much"]},

    {"id":"shoulder_cars_sequence","name":"Shoulder CARs","dose":50,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Smooth arcs, no corners.","cue_detail":"Make the circle smaller before you make it faster. Slow down through clicks.",
     "easier_title":"Smaller circles.","easier_detail":"Keep it pain-free. Speed doesn't matter. Smoothness does.",
     "harder_title":"Biggest circle you own.","harder_detail":"Tension through the full arc. Pause at the hard spots.",
     "targets":"Shoulder joint health, full range of motion maintenance",
     "why":"Controlled Articular Rotations (CARs) are the gold standard for joint health. Moving the shoulder through its complete range under tension sends a signal to the nervous system that this range is safe and should be maintained. Use it or lose it — CARs are how you keep it.",
     "how":["Stand with one arm by your side","Slowly trace the biggest circle you can with your arm","Move through every degree of the range","Slow down through any clicks or tight spots — that's where the work is"]},

    {"id":"worlds_greatest_stretch","name":"World's Greatest Stretch","dose":45,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Lunge, drop, reach.","cue_detail":"Keep the back knee off the floor if you can. Rotate from the ribcage.",
     "easier_title":"Hands stay down.","easier_detail":"Skip the rotation. Focus on the lunge and hip opening.",
     "harder_title":"Add thoracic rotation at the top.","harder_detail":"Full reach. Hold the open position for 3 breaths.",
     "targets":"Hip flexors, thoracic rotation, hamstrings, ankle mobility",
     "why":"Hits more ranges of motion in a single movement than almost any other exercise. Hip flexion, thoracic rotation, hamstring length, and ankle dorsiflexion — all in one flowing sequence.",
     "how":["Step into a deep lunge position","Drop your inside elbow toward the floor beside your front foot","Rotate your chest open and reach your arm to the ceiling","Keep the front knee stacked over the ankle throughout"]},

    # ═══ Baseline Mobility — Tail: Balance ═══
    {"id":"single_leg_balance_hold","name":"Standing Single-Leg Balance","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Stillness first.","cue_detail":"Balance over mid-foot. Let the ankle make small corrections. Eyes on one fixed point.",
     "easier_title":"Fingertips on wall.","easier_detail":"Light touch for safety. Work toward no touch.",
     "harder_title":"Eyes closed.","harder_detail":"Remove visual input. Let proprioception do the work.",
     "targets":"Proprioception, ankle stability, fall prevention",
     "why":"Single-leg balance is the most underrated predictor of healthy ageing. The ability to stand on one leg for 10+ seconds correlates with reduced fall risk and all-cause mortality. Training it for 40 seconds builds the proprioceptive feedback loop that keeps you stable.",
     "how":["Stand on one leg with a slight knee bend","Fix your gaze on one point","Let your ankle make small corrections — don't lock it","The goal is quiet stillness, not rigid freezing"]},

    {"id":"wrist_extension_lift_offs","name":"Kneeling Wrist Extensions","dose":40,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Lift clean, don't claw.","cue_detail":"Tension through forearm, not fingers. Keep knuckles relaxed.",
     "easier_title":"Less weight forward.","easier_detail":"Stay back on the knees. Gentle load on wrists.",
     "harder_title":"More weight forward. Pause at top.","harder_detail":"Lean into it. Hold the lift for 2 seconds.",
     "targets":"Wrist mobility, forearm strength, hand health",
     "why":"Modern life wrecks wrists — typing, phones, driving. Kneeling wrist extensions build extension range and forearm strength simultaneously, protecting against repetitive strain injuries and carpal tunnel symptoms.",
     "how":["Kneel on all fours with fingers pointing forward","Lean weight gently onto your palms","Lift your palms off the floor while keeping fingers down","The tension should be through the forearm, not the finger joints"]},

    {"id":"bear_crawl_hold","name":"Bear Crawl Hold","dose":30,"category":"mobility","tier":"Baseline Mobility",
     "cue_title":"Knees hover.","cue_detail":"Hands under shoulders, knees under hips. Breathe. Don't hold your breath.",
     "easier_title":"Knees touch the floor between holds.","easier_detail":"Hold for 5 seconds, rest knees, repeat.",
     "harder_title":"Hold longer. Add slow movement.","harder_detail":"Crawl forward 4 steps, back 4 steps. Knees stay hovering.",
     "targets":"Core stability, shoulder endurance, breathing under tension",
     "why":"The bear crawl hold loads your core, shoulders, and hips simultaneously while demanding you maintain a neutral spine. The key challenge is breathing normally while under isometric load.",
     "how":["Start on all fours — hands under shoulders, knees under hips","Lift your knees 1-2 inches off the floor","Hold this position while breathing normally","Don't hold your breath — that defeats the purpose"]},

    # ═══ Move — Tier 1 Foundation ═══
    {"id":"push_up","name":"Push-Up","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Chest to floor. Stop when form breaks.","cue_detail":"Elbows track 45 degrees. The moment your hips sag or neck cranes, rest in position.",
     "easier_title":"Shorter range, or hands on a surface.","easier_detail":"Lower partway, press back up. Or use a table edge for an incline push-up.",
     "harder_title":"Slow tempo. 3 seconds down.","harder_detail":"Controlled descent. Explode up. Form breaks, rest in plank.",
     "targets":"Chest, triceps, anterior deltoids, core stability",
     "why":"The push-up is the foundational upper body pressing movement. It loads the chest, shoulders, and triceps while demanding core stability throughout. 40 seconds of push-up work is enough to create a meaningful strength stimulus.",
     "how":["Hands slightly wider than shoulders, fingers spread","Lower your chest to the floor with elbows at roughly 45°","Press back up to full arm extension","The moment your hips sag or neck cranes — rest in plank position"]},

    {"id":"bodyweight_squat","name":"Bodyweight Squat","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Full depth, heels down. Go until form breaks.","cue_detail":"Sit back and down. When your back rounds or heels lift, rest standing.",
     "easier_title":"Shallower depth.","easier_detail":"No need to go below parallel. Same movement, shorter range.",
     "harder_title":"Pause squat. 3 seconds at the bottom.","harder_detail":"Full depth, hold 3 seconds, stand.",
     "targets":"Quads, glutes, full lower body strength",
     "why":"The bodyweight squat is the most fundamental lower body movement. It builds quad and glute strength while reinforcing ankle, knee, and hip mobility under load.",
     "how":["Stand with feet shoulder-width apart","Sit back and down as deep as you can control","Keep your heels on the ground throughout","When your back rounds or heels lift, rest standing"]},

    {"id":"inverted_row","name":"Inverted Row","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Chest to edge. Body stays straight.","cue_detail":"Use a door frame or table edge. When you can't clear your chest, rest hanging.",
     "easier_title":"High-angle row. More upright.","easier_detail":"Use a high surface. Pull chest to edge.",
     "harder_title":"Low-angle row. Body nearly horizontal.","harder_detail":"Feet forward, body straight. Full range.",
     "targets":"Upper back, biceps, rear deltoids, grip",
     "why":"The inverted row is the horizontal pulling counterpart to the push-up. It strengthens the upper back and biceps while correcting the forward-shoulder posture caused by desk work.",
     "how":["Find a sturdy table edge or low bar","Hang underneath with feet on the floor, body straight","Pull your chest to the edge","Lower with control — when you can't clear your chest, rest"]},

    {"id":"glute_bridge","name":"Glute Bridge","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Hips to ceiling. Squeeze at the top.","cue_detail":"Drive through your heels. When your hips drop or lower back takes over, rest on the floor.",
     "easier_title":"Two-leg bridge. Hold at the top.","easier_detail":"Drive hips up, squeeze 2 seconds.",
     "harder_title":"Elevated feet. Heels on chair.","harder_detail":"Greater hip range. Drive through heels.",
     "targets":"Glutes, hamstrings, hip extension, lower back support",
     "why":"The glute bridge activates the posterior chain — the muscles most inhibited by sitting. Strong glutes protect the lower back, stabilise the pelvis, and power every lower body movement.",
     "how":["Lie on your back, knees bent, feet flat on the floor","Drive your hips toward the ceiling by pressing through your heels","Squeeze your glutes hard at the top — full hip extension","Lower with control. When your back takes over, rest on the floor"]},

    {"id":"hollow_body_hold","name":"Hollow Body Hold","dose":30,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Low back pressed flat. Hold until it lifts.","cue_detail":"Arms overhead, legs extended. The moment your lower back lifts, rest flat.",
     "easier_title":"Bend knees. Arms by your sides.","easier_detail":"Same flat-back position, shorter lever.",
     "harder_title":"Hollow body rock. Hold and rock.","harder_detail":"Same shape, add a gentle rock.",
     "targets":"Deep core, anterior chain, spinal stability",
     "why":"The hollow body hold is the foundation of all gymnastics core work. It trains the anterior chain to create and maintain a rigid, slightly curved shape. The minimum effective dose is just 30 seconds because the isometric demand is high.",
     "how":["Lie on your back, arms overhead, legs extended","Press your lower back into the floor — this is non-negotiable","Lift your arms and legs slightly off the ground","The moment your lower back peels off the floor, rest"]},

    {"id":"sit_to_stand","name":"Sit-to-Stand","dose":30,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Chair height. Control the sit.","cue_detail":"Lower slowly, pause, stand. When you can't control the descent, rest seated.",
     "easier_title":"Higher surface. Armrest assist.","easier_detail":"Use a higher chair or push off armrests.",
     "harder_title":"Lower surface. No hands.","harder_detail":"Low chair or step. Arms crossed.",
     "targets":"Functional leg strength, independence, quad endurance",
     "why":"The sit-to-stand is the most functional exercise in any program. The ability to lower yourself to a chair and stand back up without assistance is a primary marker of functional independence. Three seconds down is the target tempo.",
     "how":["Stand in front of a chair","Lower yourself slowly over 3 seconds","Pause briefly at the bottom","Stand back up with control"]},

    {"id":"reverse_lunge","name":"Reverse Lunge","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Step back, knee to floor. Alternate legs.","cue_detail":"Front knee tracks over toes. When you stumble or can't control the descent, rest standing.",
     "easier_title":"Assisted. Hold a wall or chair.","easier_detail":"Step back with support. Focus on control.",
     "harder_title":"Slow tempo. 3 seconds down.","harder_detail":"Controlled descent each rep.",
     "targets":"Quads, glutes, single-leg stability, balance",
     "why":"The reverse lunge builds single-leg strength without the knee stress of a forward lunge. Stepping backward loads the front leg eccentrically while training balance and hip stability.",
     "how":["Stand tall, then step one foot straight back","Lower your back knee toward the floor with control","Front knee stays stacked over the ankle","Drive through the front heel to return to standing"]},

    {"id":"superman_hold","name":"Superman Hold","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Lift arms and legs off the floor. Hold.","cue_detail":"Face down, everything lifts. When your chest drops or you lose the squeeze, rest flat.",
     "easier_title":"Half superman. Lift arms only, then legs only.","easier_detail":"Alternate: arms up, then legs up.",
     "harder_title":"Superman with pull. Arms sweep back.","harder_detail":"Lift everything, then pull elbows to ribs.",
     "targets":"Lower back, glutes, posterior chain endurance",
     "why":"The superman hold strengthens the entire posterior chain — lower back, glutes, and upper back — in one isometric position. It's the back-body counterpart to the hollow body hold.",
     "how":["Lie face down, arms extended overhead","Lift arms, chest, and legs off the floor simultaneously","Hold the position while breathing normally","When your chest drops or you lose the squeeze, rest flat"]},

    {"id":"side_plank_hold","name":"Side Plank Hold","dose":40,"category":"bodyweight","tier":"Bodyweight — Foundation",
     "cue_title":"Stack and hold. No sagging.","cue_detail":"Bottom hip stays lifted. Hips drop, rest, then switch sides.",
     "easier_title":"Hold for 10 seconds, rest 5.","easier_detail":"Same stacked alignment, shorter intervals.",
     "harder_title":"Top leg lifted. Hold.","harder_detail":"Raise the top leg. Everything else stays stacked.",
     "targets":"Obliques, lateral hip stability, spinal health",
     "why":"The side plank builds lateral core stability. Weak obliques are a leading contributor to lower back pain. McGill's research identifies the side plank as one of the 'Big Three' exercises for spinal health.",
     "how":["Lie on your side, elbow under your shoulder","Stack your hips and lift them off the ground","Maintain a straight line from head to feet","When your hips sag, rest and switch sides"]},

    # ═══ Move — Tier 2 Build ═══
    {"id":"single_leg_glute_bridge","name":"Single-Leg Glute Bridge","dose":35,"category":"bodyweight","tier":"Bodyweight — Build",
     "cue_title":"One leg drives. Hips stay level.","cue_detail":"Extend the free leg. Drive through the planted heel. When hips twist or drop, rest.",
     "easier_title":"Foot stays closer. Shorter lever.","easier_detail":"Free foot rests on the planted knee.",
     "harder_title":"Free leg straight up. Slow tempo.","harder_detail":"Full extension. 3 seconds up, 3 seconds down.",
     "targets":"Unilateral glute strength, pelvic stability",
     "why":"The single-leg version doubles the load on each glute and exposes any asymmetry between sides. Pelvic stability on one leg is essential for walking, running, and stair climbing.",
     "how":["Lie on your back, one foot planted, the other extended","Drive your hips up through the planted heel","Keep your hips level — no twisting","Lower with control and switch sides"]},

    # ═══ Move — Tier 3 Strength ═══
    {"id":"pike_push_up","name":"Pike Push-Up","dose":35,"category":"bodyweight","tier":"Bodyweight — Strength",
     "cue_title":"Hips high. Head touches floor.","cue_detail":"V-shape body. Elbows track back, not out.",
     "easier_title":"Shallower pike angle.","easier_detail":"Feet closer to hands. Less shoulder load.",
     "harder_title":"Feet elevated pike.","harder_detail":"Feet on a chair. Steeper angle, more overhead press demand.",
     "targets":"Shoulders, triceps, overhead pressing strength",
     "why":"The pike push-up is the bridge between a regular push-up and a handstand push-up. By elevating your hips into a V-shape, the load shifts onto the shoulders.",
     "how":["Start in a push-up position, then walk your feet toward your hands","Create a V-shape with hips high in the air","Lower your head toward the floor by bending your elbows","Press back up. When you can't clear your head, rest in pike position"]},

    {"id":"bulgarian_split_squat","name":"Bulgarian Split Squat","dose":40,"category":"bodyweight","tier":"Bodyweight — Strength",
     "cue_title":"Rear foot elevated. Front knee tracks.","cue_detail":"Use a chair or step. Lower until back knee nears floor.",
     "easier_title":"Lower rear foot. Hand on wall.","easier_detail":"Use a low step. Support for balance.",
     "harder_title":"Pause at the bottom. 3 seconds.","harder_detail":"No bounce out of the hole. Hold and drive.",
     "targets":"Quads, glutes, single-leg strength, balance",
     "why":"The Bulgarian split squat is the most effective single-leg strength exercise. Elevating the rear foot shifts nearly all the load onto the front leg, building unilateral strength that transfers directly to running, climbing, and injury prevention.",
     "how":["Place your rear foot on a chair or step behind you","Lower your back knee toward the floor","Front knee tracks over your toes","Drive through the front heel to stand"]},

    {"id":"single_leg_rdl","name":"Single-Leg Romanian Deadlift","dose":35,"category":"bodyweight","tier":"Bodyweight — Strength",
     "cue_title":"Hip hinge on one leg. Spine stays long.","cue_detail":"Free leg reaches back as torso tips forward. How far you go matters less than keeping the spine long.",
     "easier_title":"Fingertips on wall. Shallower hinge.","easier_detail":"Support for balance. Feel the hamstring, don't chase depth.",
     "harder_title":"Arms overhead. Full depth.","harder_detail":"Longer lever, more demand. Torso parallel to floor.",
     "targets":"Hamstrings, glutes, single-leg balance, posterior chain",
     "why":"The single-leg RDL is one of the most functional exercises in any program. It trains the hip hinge on one leg — the same pattern used in picking things up, climbing, and running.",
     "how":["Stand on one leg with a slight knee bend","Hinge forward at the hip — free leg extends behind you","Keep your spine long and hips square","How far you go matters less than maintaining a straight back"]},

    {"id":"side_plank_hip_dip","name":"Side Plank with Hip Dip","dose":35,"category":"bodyweight","tier":"Bodyweight — Strength",
     "cue_title":"Lower hip, then drive it back up.","cue_detail":"Controlled dip, not a collapse. Drive-up stalls, rest and switch.",
     "easier_title":"Shorter intervals. Dip and drive for 10 seconds.","easier_detail":"Same movement, timed bursts.",
     "harder_title":"Add top arm reach overhead.","harder_detail":"Dip, drive, and reach. More oblique demand.",
     "targets":"Obliques, lateral core strength, hip stability",
     "why":"Adding the hip dip to a side plank converts a static hold into a dynamic strengthening exercise. The controlled lowering and driving builds oblique strength through a full range of motion.",
     "how":["Set up in a side plank position","Lower your bottom hip toward the floor with control","Drive it back up to full extension","When you can't control the dip or drive, rest and switch"]},

    {"id":"deficit_reverse_lunge","name":"Deficit Reverse Lunge","dose":35,"category":"bodyweight","tier":"Bodyweight — Strength",
     "cue_title":"Front foot elevated. Step back deeper.","cue_detail":"Small step or book under front foot. Greater range = more glute demand.",
     "easier_title":"Smaller deficit. Use support.","easier_detail":"Thin book under front foot. Hand on wall.",
     "harder_title":"Higher deficit. No support.","harder_detail":"Full step height. Arms free.",
     "targets":"Glutes, quads, hip range of motion under load",
     "why":"Elevating the front foot increases the range of motion at the hip, demanding more from the glutes and building strength through a deeper range than a standard lunge.",
     "how":["Stand on a small step or thick book","Step one foot back and lower your knee toward the floor","The deficit creates a deeper stretch at the bottom","Control the descent — when you can't, rest standing"]},

    # ═══ Move — Tier 4 Power ═══
    {"id":"decline_push_up","name":"Decline Push-Up","dose":35,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Feet elevated. More shoulder load.","cue_detail":"Chair or step under feet. Chest to floor. Hips sag or neck cranes, rest in plank.",
     "easier_title":"Low elevation. Same form.","easier_detail":"Small step under feet. Less load on shoulders.",
     "harder_title":"High elevation. Slow tempo.","harder_detail":"Chair or high step. 3 seconds down, explode up.",
     "targets":"Upper chest, shoulders, triceps, core",
     "why":"Elevating the feet shifts more load onto the upper chest and shoulders — bridging the gap between flat push-ups and pike push-ups. The decline position also increases core demand.",
     "how":["Place your feet on a chair or step","Set up in a push-up position with hands on the floor","Lower your chest to the floor","Press back up — when hips sag, rest in plank"]},

    {"id":"assisted_pistol_squat","name":"Assisted Pistol Squat","dose":30,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"One leg. Hold something for balance.","cue_detail":"Door frame or chair for support. Full depth on one leg.",
     "easier_title":"Both hands on support. Shallow depth.","easier_detail":"Door frame for full support. Go as deep as you can control.",
     "harder_title":"Light fingertip assist only.","harder_detail":"Minimal support. Nearly freestanding.",
     "targets":"Single-leg strength, balance, ankle mobility",
     "why":"The assisted pistol squat builds toward the full pistol by allowing you to practice the movement pattern with support. It develops the single-leg strength, balance, and ankle dorsiflexion needed for the unassisted version.",
     "how":["Hold a door frame or chair with one or both hands","Stand on one leg and extend the other forward","Lower as deep as you can with control","Use the support as needed — less over time"]},

    {"id":"negative_pull_up","name":"Negative Pull-Up","dose":25,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Jump to top. Lower for 5 seconds.","cue_detail":"Chin over bar, then slow descent. When you can't control the lower, rest hanging.",
     "easier_title":"Slower jump, 3-second lower.","easier_detail":"Shorter eccentric. Build control before time.",
     "harder_title":"8-second lower. Pause halfway.","harder_detail":"Elbows at 90°, hold 2 seconds, then continue down.",
     "targets":"Lats, biceps, grip, eccentric pulling strength",
     "why":"Eccentric (lowering) training builds strength faster than concentric training. The negative pull-up lets you train the pulling muscles at loads you can't yet lift — it's the most effective way to build toward a full pull-up.",
     "how":["Jump or step up to get your chin over the bar","Lower yourself as slowly as possible — target 5 seconds","Control the entire descent to a full dead hang","When you can't slow the drop, rest hanging"]},

    {"id":"nordic_curl","name":"Nordic Curl","dose":25,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Anchor feet. Lower slowly.","cue_detail":"Knees on floor, feet under couch. Lean forward as slow as possible. Catch yourself, reset.",
     "easier_title":"Hands catch early. Shorter range.","easier_detail":"Fall forward less far. Catch yourself sooner.",
     "harder_title":"Full range. Push off floor to reset.","harder_detail":"Lower as far as possible, push off floor to return.",
     "targets":"Hamstrings, eccentric knee flexion, injury prevention",
     "why":"The Nordic curl is the most evidence-backed exercise for hamstring injury prevention. The eccentric loading at long muscle lengths builds the hamstring strength that protects against strains during running and sprinting.",
     "how":["Kneel on the floor with feet anchored under something heavy","Lean forward slowly, keeping your body straight","Catch yourself with your hands when you can't control the descent","Push off the floor to reset — progress is measured in seconds, not reps"]},

    {"id":"l_sit_hold","name":"L-Sit Hold","dose":20,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Hands press down. Legs lift.","cue_detail":"On floor or books. Compress hard: hips lift, legs extend. Legs drop, rest seated.",
     "easier_title":"Tucked L-sit. Knees bent.","easier_detail":"Lift hips with knees tucked. Build toward straight legs.",
     "harder_title":"Full L-sit. Legs straight and parallel.","harder_detail":"Max compression. Legs parallel to floor.",
     "targets":"Core compression, hip flexor strength, tricep endurance",
     "why":"The L-sit demands extreme core compression and hip flexor strength simultaneously. It's a gymnastics fundamental that builds the anterior chain strength needed for advanced bodyweight movements.",
     "how":["Sit on the floor with legs extended, hands beside your hips","Press your hands into the floor and lift your hips","Extend your legs in front of you","When your legs drop below parallel, rest seated"]},

    {"id":"single_leg_calf_raise","name":"Single-Leg Calf Raise","dose":40,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Full range. Slow up, slow down.","cue_detail":"On a step edge if possible. Pause at the top.",
     "easier_title":"From flat floor. Both legs if needed.","easier_detail":"No step edge. Reduce range.",
     "harder_title":"Full range off step edge. Pause at top and bottom.","harder_detail":"2-second holds at top and bottom.",
     "targets":"Calf strength, Achilles tendon health, ankle stability",
     "why":"Calves need higher volume than most muscles to adapt (Hébert-Losier 2009). Single-leg calf raises build the soleus and gastrocnemius strength that protects the Achilles tendon and powers walking, running, and jumping.",
     "how":["Stand on one leg, ideally on a step edge","Rise up onto your toes as high as possible","Lower slowly below the step edge for full range","Pause at the top — the bottom range off a step is where adaptation happens"]},

    {"id":"archer_push_up","name":"Archer Push-Up","dose":30,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"One arm works. The other assists.","cue_detail":"Wide hands. Lower toward one hand. Assist arm stays straight.",
     "easier_title":"Less lean. More assist arm help.","easier_detail":"Bend assist arm slightly. Share more load.",
     "harder_title":"Full lean. Assist arm fingertips only.","harder_detail":"Near-single-arm push-up.",
     "targets":"Unilateral chest and tricep strength, pushing power",
     "why":"The archer push-up is the progression toward a one-arm push-up. It loads one arm significantly more than the other, building unilateral pushing strength and exposing any imbalance between sides.",
     "how":["Set up with hands wide apart","Lower your chest toward one hand","The working arm bends while the assist arm stays relatively straight","Press back up — when form breaks, rest in plank"]},

    {"id":"dragon_flag_partial","name":"Dragon Flag","dose":20,"category":"bodyweight","tier":"Bodyweight — Power",
     "cue_title":"Hold the bench. Lower your body as one unit.","cue_detail":"Tuck or extend legs. Lower until you lose the rigid line.",
     "easier_title":"Tucked position. Shorter lever.","easier_detail":"Knees tucked tight. Lower and raise just the hips.",
     "harder_title":"Full extension. Straight body.","harder_detail":"Legs extended, body rigid. Lower to horizontal and back.",
     "targets":"Full anterior chain, advanced core strength",
     "why":"The dragon flag is one of the most demanding core exercises. It trains the entire anterior chain to maintain rigidity against gravity — the same skill needed for handstands, levers, and advanced bodyweight movements.",
     "how":["Lie on a bench and grip the edge behind your head","Lift your body into a straight line, supported by your upper back","Lower your body as one rigid unit toward the bench","When you lose the straight line, rest flat"]},

    # ═══ Move — Tier 5 Apex ═══
    {"id":"handstand_push_up_wall","name":"Handstand Push-Up (Wall)","dose":20,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"Kick up. Lower to head. Press.","cue_detail":"Wall-supported. Head touches floor, then press up.",
     "easier_title":"Partial range. Head to pad.","easier_detail":"Use a pillow to shorten range. Same form, less depth.",
     "harder_title":"Full range. Deficit if possible.","harder_detail":"Head to floor or hands on blocks for extra range.",
     "targets":"Overhead pressing strength, shoulder power, core stability",
     "why":"The handstand push-up is the ultimate bodyweight pressing exercise. It loads the shoulders and triceps with your full bodyweight in an overhead position — building the kind of pressing strength that no other bodyweight exercise can match.",
     "how":["Kick up into a handstand against a wall","Lower your head toward the floor","Press back up to full arm extension","When you can't press, walk down safely"]},

    {"id":"pistol_squat","name":"Pistol Squat","dose":25,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"One leg. No assistance. Full depth.","cue_detail":"Free leg extends forward. Sit all the way down, stand all the way up.",
     "easier_title":"Sit to low surface.","easier_detail":"Use a low chair as depth target. Control down, stand up.",
     "harder_title":"Full depth. Pause at bottom. Arms forward.","harder_detail":"Rock-bottom, hold 2 seconds, drive up.",
     "targets":"Maximum single-leg strength, mobility, balance",
     "why":"The pistol squat demands full single-leg strength, ankle mobility, hip flexibility, and balance simultaneously. It's the gold standard of lower body bodyweight mastery.",
     "how":["Stand on one leg, extend the other forward","Lower yourself all the way to the bottom","Stand back up without assistance","Free leg stays off the floor throughout"]},

    {"id":"pull_up","name":"Pull-Up","dose":25,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"Dead hang to chin over bar.","cue_detail":"Full range. No kipping. When you can't clear your chin, rest hanging.",
     "easier_title":"Band-assisted or partial range.","easier_detail":"Use a resistance band or start from half-hang.",
     "harder_title":"Slow negative. 5 seconds down.","harder_detail":"Full pull, then 5-second controlled lower.",
     "targets":"Lats, biceps, grip, upper back",
     "why":"The pull-up is the gold standard of upper body pulling strength. It loads the entire back, biceps, and grip in a single compound movement. The minimum dose is just 25 seconds because each rep carries a very high strength stimulus.",
     "how":["Hang from a bar with palms facing away, slightly wider than shoulders","Pull your chin over the bar by driving your elbows down and back","Lower with control to a full dead hang","No kipping or swinging — strict form only"]},

    {"id":"shrimp_squat","name":"Shrimp Squat","dose":25,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"Grab rear foot. Kneel down on one leg.","cue_detail":"Rear knee touches floor behind you. Stand up.",
     "easier_title":"Hand on wall. Shallow range.","easier_detail":"Support for balance. Knee doesn't need to touch floor.",
     "harder_title":"No support. Full depth. Pause.","harder_detail":"Rear knee touches floor, pause 1 second, drive up.",
     "targets":"Quad strength, balance, single-leg control",
     "why":"The shrimp squat loads the quads more than the pistol squat due to the rear leg position. It demands knee flexion strength and balance in a pattern that most people have never trained.",
     "how":["Stand on one leg and grab the other foot behind you","Lower your back knee toward the floor","Touch the knee down with control","Stand back up — the quad tension and balance are the challenge"]},

    {"id":"muscle_up_negative","name":"Muscle-Up Negative","dose":20,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"Start on top of bar. Lower through transition.","cue_detail":"Slow descent from support to hang. The transition is the exercise.",
     "easier_title":"Focus on the dip portion.","easier_detail":"Slow lower from support to chest level only.",
     "harder_title":"Full transition. Slowest possible.","harder_detail":"8-second lower through the transition point.",
     "targets":"Transition strength, chest, triceps, lats, pulling power",
     "why":"The muscle-up transition is the most technically demanding bodyweight movement. Training the negative (lowering) phase builds the strength and control through the transition point that most people lack.",
     "how":["Start in a support position on top of a bar","Slowly lower yourself through the transition point","Control the entire descent from support to hang","The transition is the exercise — slow down through it"]},

    {"id":"l_sit_tuck_planche","name":"L-Sit to Tuck Planche","dose":20,"category":"bodyweight","tier":"Bodyweight — Apex",
     "cue_title":"L-sit, then lean forward to tuck.","cue_detail":"Shift weight onto hands, tuck knees toward chest. Hold the lean.",
     "easier_title":"L-sit only. Lean forward slightly.","easier_detail":"Don't commit to the planche lean. Just find the forward shift.",
     "harder_title":"Hold tuck planche for 3 seconds.","harder_detail":"Full lean, tucked knees, hold the position.",
     "targets":"Planche progression, shoulder strength, core compression",
     "why":"The transition from L-sit to tuck planche teaches the forward lean and shoulder protraction needed for planche work. It builds the straight-arm pushing strength unique to gymnastics.",
     "how":["Start in an L-sit position on the floor or parallettes","Lean your shoulders forward over your hands","Tuck your knees toward your chest as you lean","Hold the tuck planche position — when you collapse, return to L-sit"]},

    # ═══ Recovery ═══
    {"id":"hang","name":"Hang","dose":55,"category":"recovery","tier":"Recovery",
     "cue_title":"Decompress.","cue_detail":"Light grip, long spine. No shoulder shrugging. Let the weight of your arms do the work.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Spinal decompression, shoulder opening, grip endurance",
     "why":"A passive hang decompresses the spine after exercise, opening up space between vertebrae and allowing the shoulder joint to stretch under gentle load. Used as a recovery tool rather than a mobility exercise.",
     "how":["Find a bar and hang with a relaxed grip","Let your body go heavy — no shrugging","Breathe normally","Let the weight of your body do the work"]},

    {"id":"supine_lumbar_rotations","name":"Supine Lumbar Rotations","dose":40,"category":"recovery","tier":"Recovery",
     "cue_title":"Lower ribs melt down.","cue_detail":"Let gravity rotate you. Breathe out and soften, don't force range.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Lumbar spine mobility, lower back relief, spinal decompression",
     "why":"Gentle rotations in a supine position allow the lower back to decompress without load. Gravity does the work — each exhale is permission to go a little further, not a demand.",
     "how":["Lie on your back with knees bent","Let both knees fall to one side","Breathe out and let gravity deepen the rotation","Switch sides slowly — no forcing"]},

    {"id":"wall_butterfly","name":"Supine Wall Butterfly","dose":30,"category":"recovery","tier":"Recovery",
     "cue_title":"Knees drop gently.","cue_detail":"Back stays heavy on the wall. Let the inner thighs release gradually.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Inner thigh release, hip opening, nervous system calming",
     "why":"The wall butterfly uses gravity and the wall to passively open the hips without any muscular effort. It's a recovery position that lets the adductors release while the supported position calms the nervous system.",
     "how":["Lie on your back with legs up the wall","Bring the soles of your feet together, knees dropping out","Let gravity open your hips — no pushing","Breathe and let the inner thighs release gradually"]},

    {"id":"supported_jefferson_stretch","name":"Supported Jefferson Stretch","dose":40,"category":"recovery","tier":"Recovery",
     "cue_title":"Assisted control.","cue_detail":"Hands help. No hanging weight. You get the spinal articulation without the loading demand.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Posterior chain release, spinal articulation, gentle decompression",
     "why":"A gentler version of the Jefferson curl that uses hand support to remove the loading demand. You get the spinal articulation and posterior chain stretch without the nervous system tension of unsupported end-range flexion.",
     "how":["Stand with hands on a support","Roll down through the spine one vertebra at a time","Let your hands assist — no hanging weight","Roll back up the same way — sequential and controlled"]},

    {"id":"long_exhale_breathing","name":"Long Exhale Breathing","dose":25,"category":"recovery","tier":"Recovery",
     "cue_title":"Exhale longer than you inhale.","cue_detail":"Let ribs soften down. No forcing. Just a longer out-breath.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Parasympathetic activation, heart rate reduction, nervous system regulation",
     "why":"Extended exhales activate the vagus nerve, shifting your nervous system from fight-or-flight to rest-and-digest. This is the simplest, most evidence-backed breathing technique for immediate stress reduction.",
     "how":["Breathe in through your nose for a natural count","Breathe out for roughly twice as long","No forcing — let the exhale be passive and soft","Focus on the ribs softening down with each breath out"]},

    # ═══ Focus Prepends ═══
    {"id":"gentle_neck_rotations","name":"Gentle Neck Rotations","dose":30,"category":"mobility","tier":"Focus — Neck",
     "cue_title":"Easy arcs.","cue_detail":"Stop well before stretch. Let the neck find its own range. Move within total comfort.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Neck mobility, cervical spine health, tension relief",
     "why":"Gentle neck rotations maintain cervical range of motion and relieve tension from desk work. The key is staying within comfortable range — the neck responds better to gentle, frequent movement than aggressive stretching.",
     "how":["Slowly rotate your head side to side","Stop well before any stretch or discomfort","Let the neck find its own range","Move within total comfort — range is not the goal"]},

    {"id":"chin_tucks","name":"Chin Tucks","dose":40,"category":"mobility","tier":"Focus — Neck",
     "cue_title":"Double chin. Hold gently.","cue_detail":"Draw the chin straight back, not down. Feel the back of the neck lengthen. Hold 5 seconds, release.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Deep cervical flexor activation, forward head posture correction",
     "why":"Chin tucks activate the deep cervical flexors — the muscles that counteract forward head posture. The Jull protocol (10 reps × 5s hold) is the research-backed standard for cervical stabilisation.",
     "how":["Sit or stand with good posture","Draw your chin straight back — not down","Create a 'double chin' position","Hold for 5 seconds, release, repeat 8-10 times"]},

    {"id":"shoulder_dislocates","name":"Shoulder Pass-Overs","dose":35,"category":"mobility","tier":"Focus — Shoulder",
     "cue_title":"Wide grip. Slow arc.","cue_detail":"Use a towel or band. Only go as far as control allows. Wider grip is easier.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Shoulder range of motion, overhead mobility, rotator cuff health",
     "why":"Shoulder pass-overs take the joint through its full range of motion under gentle tension. It's the most effective way to maintain overhead mobility and keep the rotator cuff healthy.",
     "how":["Hold a towel or band with a wide grip","Slowly pass it over your head and behind your back","Only go as far as you can control","Wider grip is easier — narrow it as you earn the range"]},

    {"id":"knee_to_wall_ankle_stretch","name":"Knee-to-Wall Ankle Stretch","dose":35,"category":"mobility","tier":"Focus — Ankle",
     "cue_title":"Knee tracks over toes.","cue_detail":"Heel stays down. Slow push, then release. Push until the heel almost lifts, then back off.",
     "easier_title":None,"easier_detail":None,"harder_title":None,"harder_detail":None,
     "targets":"Ankle dorsiflexion, squat depth, knee health",
     "why":"Limited ankle dorsiflexion is the number one limiter of squat depth. The knee-to-wall stretch is the most effective way to improve it — push the knee forward over the toes while keeping the heel down.",
     "how":["Stand facing a wall with one foot a few inches back","Push your knee forward toward the wall","Keep your heel firmly on the ground","Push until the heel almost lifts, then back off — that edge is where the range is"]},
]

# ─────────────────────────────────────────────
# SHIFT DATA (from ShiftProtocol.swift)
# ─────────────────────────────────────────────

shift_modes = [
    {"id":"arrive","title":"Arrive","state_from":"Scattered","state_to":"Present",
     "color_hex":"#6366F1","color_var":"var(--indigo)",
     "breath_label":"4 seconds in, 6 seconds out",
     "breath_html":'<span class="breath-phase" style="background:rgba(99,102,241,.15);color:var(--indigo)">4s in</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(99,102,241,.15);color:var(--indigo)">6s out</span>',
     "cycle":"10s","dose":90,"min_duration":"2 min",
     "description":"Arrive brings your attention back into your body. It uses a longer exhale to activate your parasympathetic nervous system \u2014 the part that calms you down.",
     "example":"Use when you're distracted, restless, or can't settle into what's in front of you.",
     "science":"The 4:6 ratio creates a resonance frequency in heart rate variability. Your heart rate rises on the inhale and falls on the exhale \u2014 when the exhale is longer, net parasympathetic tone increases. Research (Lehrer & Gevirtz, 2014) shows HRV changes begin at 60\u201390 seconds of coherent breathing. Nine full cycles at 10 seconds each gives the baroreflex time to entrain.",
     "physical_cues":["Press your feet flat into the floor. Feel the ground push back.","Let your palms rest wherever they fall. Stop arranging yourself.","Scan from your jaw to your shoulders. Wherever you're gripping, let it soften.","Let your hands go heavy. You don't need to hold anything right now."],
     "attention_lines":["You're already here.","Nothing needs your attention but this.","Stop reaching forward. You've arrived.","The only place you need to be is this one."],
     "font_family":"'JosefinSans-ThinItalic', sans-serif"},

    {"id":"prime","title":"Prime","state_from":"Flat","state_to":"Warm",
     "color_hex":"#EAB308","color_var":"var(--solar)",
     "breath_label":"3 seconds in, 3 seconds out",
     "breath_html":'<span class="breath-phase" style="background:rgba(234,179,8,.15);color:var(--solar)">3s in</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(234,179,8,.15);color:var(--solar)">3s out</span>',
     "cycle":"6s","dose":60,"min_duration":"1 min",
     "description":"Prime wakes your body up without forcing it. Equal-length breathing raises your baseline arousal and brings warmth to your system.",
     "example":"Use when you feel flat, sluggish, or need to show up with more energy.",
     "science":"Equal-ratio breathing (sama vritti) activates the sympathetic nervous system without tipping into stress. The faster 6-second cycle increases respiratory rate, which raises heart rate, skin conductance, and alertness. Research (Harbour et al., 2022) confirms sympathetic upregulation begins at 30\u201345 seconds.",
     "physical_cues":["Rub your palms together briskly. Feel the heat build.","Tap your chest with your fingertips. Light, quick, like rain.","Shake your hands out loosely. Let your wrists go floppy.","Stop moving. Notice what's buzzing. That's your system waking up."],
     "attention_lines":["Energy doesn't need a reason. Let it come.","Let your body warm itself.","Stop waiting to feel ready. This is ready."],
     "font_family":"'Unbounded-Black', sans-serif"},

    {"id":"reset","title":"Reset","state_from":"Depleted","state_to":"Restored",
     "color_hex":"#67E8F9","color_var":"var(--ice)",
     "breath_label":"4 seconds in, sip, 8 seconds out",
     "breath_html":'<span class="breath-phase" style="background:rgba(103,232,249,.12);color:var(--ice)">4s in</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(103,232,249,.12);color:var(--ice)">sip</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(103,232,249,.12);color:var(--ice)">8s out</span>',
     "cycle":"14s","dose":60,"min_duration":"2 min",
     "description":"Reset uses a physiological sigh \u2014 a double inhale followed by a long exhale. This is the fastest known way to reduce stress in real time.",
     "example":"Use after a stressful meeting, a difficult conversation, or when you feel wrung out.",
     "science":"The physiological sigh (double inhale + extended exhale) was identified by Stanford researchers as the fastest real-time stress reducer. The sip re-inflates collapsed alveoli in the lungs, maximising CO\u2082 offloading on the long exhale. Just 4 full sigh cycles (~60 seconds) produce measurable cortisol reduction.",
     "physical_cues":["Press your temples with your fingertips and rotate gently.","Move your fingertips to your scalp. Slow circles, medium pressure.","Let your jaw drop open. Teeth apart, lips soft.","Release your tongue from the roof of your mouth. Let it rest."],
     "attention_lines":["You're gripping something. Let it pass through.","Your body doesn't need your permission to let go.","The sigh does the work. You just breathe."],
     "font_family":"'FragmentMono-Italic', monospace"},

    {"id":"downshift","title":"Downshift","state_from":"On","state_to":"Off",
     "color_hex":"#A78BFA","color_var":"var(--lavender)",
     "breath_label":"4 seconds in, 8 seconds out",
     "breath_html":'<span class="breath-phase" style="background:rgba(167,139,250,.12);color:var(--lavender)">4s in</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(167,139,250,.12);color:var(--lavender)">8s out</span>',
     "cycle":"12s","dose":120,"min_duration":"3 min",
     "description":"Downshift is for winding down completely. The exhale is twice the inhale, which progressively lowers your heart rate and signals safety to your nervous system.",
     "example":"Use before sleep, after a long day, or when you need to fully switch off.",
     "science":"The 1:2 inhale-to-exhale ratio is the classic parasympathetic breathing pattern. Each extended exhale stimulates the vagus nerve, progressively lowering heart rate and blood pressure. Deep parasympathetic deactivation requires at least 10 full cycles (120 seconds).",
     "physical_cues":["Place one hand on your chest. Feel it rise and fall.","Notice the warmth spreading under your hand. Stay with it.","Drop your shoulders away from your ears. Stop holding them up.","Let your whole body get heavy. Sink into whatever's holding you.","Soften your forehead, your jaw, your eyes. Unclench everything."],
     "attention_lines":["You're still managing. Stop.","There's nothing left to resist.","Let yourself be done.","You've done enough today."],
     "font_family":"'Fraunces-LightItalic', serif"},

    {"id":"override","title":"Override","state_from":"Overwhelm","state_to":"Control",
     "color_hex":"#EF4444","color_var":"var(--red)",
     "breath_label":"2.5 seconds in, 1.5 seconds out \u00d7 40 breaths",
     "breath_html":'<span class="breath-phase" style="background:rgba(239,68,68,.12);color:var(--red)">2.5s in</span><span class="breath-arrow">\u2192</span><span class="breath-phase" style="background:rgba(239,68,68,.12);color:var(--red)">1.5s out</span><span class="breath-arrow">\u00d7 40</span>',
     "cycle":"4s","dose":140,"min_duration":"3 min",
     "description":"Override uses deep, rhythmic breathing to shift your nervous system out of overwhelm. Forty breaths to flood your system with oxygen. Then you hold, and your body resets.",
     "example":"Use when you're overwhelmed, panicking, or need to take back control right now.",
     "science":"Cyclic hyperventilation (40 controlled breaths at a fast cadence) temporarily changes blood chemistry \u2014 reducing CO\u2082 and increasing blood pH. This produces tingling, lightheadedness, and a powerful shift in autonomic state. The subsequent breath hold leverages the dive reflex, triggering a vagal brake that brings heart rate down sharply.",
     "physical_cues":[],"attention_lines":[],
     "font_family":"'BigShoulders-Black', sans-serif"},
]


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def slug(id_str):
    return id_str.replace("_", "-")

def format_dose(seconds):
    if seconds >= 60:
        m = seconds // 60
        s = seconds % 60
        return f"{m}:{s:02d}" if s else f"{m} min"
    return f"{seconds}s"

CATEGORY_COLORS = {
    "mobility": ("var(--green)", "rgba(48,209,88,.12)"),
    "bodyweight": ("var(--tangerine)", "rgba(255,111,44,.12)"),
    "recovery": ("var(--steel)", "rgba(142,150,168,.12)"),
}
CATEGORY_LABELS = {
    "mobility": "Mobility",
    "bodyweight": "Bodyweight Strength",
    "recovery": "Recovery",
}


def video_html(ex_id, category="mobility"):
    """Return video element if video exists, else empty string."""
    if ex_id in available_videos:
        return f'''
    <div class="guide-figure" data-category="{category}">
      <video autoplay loop muted playsinline>
        <source src="../assets/video/{ex_id}.mp4" type="video/mp4">
      </video>
    </div>'''
    return ""


def exercise_page(ex):
    s = slug(ex["id"])
    color, bg = CATEGORY_COLORS[ex["category"]]
    cat_label = CATEGORY_LABELS[ex["category"]]
    dose_fmt = format_dose(ex["dose"])
    title = f'{ex["name"]}: Minimum Effective Dose | Baseline'
    desc = f'{ex["name"]} \u2014 {ex["targets"]}. Minimum effective dose: {dose_fmt}. Learn the science, form cues, and variants.'

    steps_html = "".join(f"<li>{h.escape(step)}</li>" for step in ex["how"])

    variants_html = ""
    if ex.get("easier_title"):
        variants_html = f'''
    <div class="content-section">
      <h2>Variants</h2>
      <div class="variant-grid">
        <div class="variant-card">
          <div class="variant-label easier">Easier</div>
          <div class="variant-title">{h.escape(ex["easier_title"])}</div>
          <div class="variant-desc">{h.escape(ex["easier_detail"])}</div>
        </div>
        <div class="variant-card">
          <div class="variant-label harder">Harder</div>
          <div class="variant-title">{h.escape(ex["harder_title"])}</div>
          <div class="variant-desc">{h.escape(ex["harder_detail"])}</div>
        </div>
      </div>
    </div>'''

    vid = video_html(ex["id"], ex["category"])

    related = [e for e in exercises if e["category"] == ex["category"] and e["id"] != ex["id"]][:4]
    related_html = ""
    if related:
        cards = "".join(f'''<a class="related-card" href="{slug(r["id"])}.html">
        <div class="related-name">{h.escape(r["name"])}</div>
        <div class="related-dose">Dose: {format_dose(r["dose"])}</div>
      </a>''' for r in related)
        related_html = f'''
    <div class="content-section">
      <h2>Related exercises</h2>
      <div class="related-grid">{cards}</div>
    </div>'''

    steps_json = ",".join('{"@type":"HowToStep","text":"' + h.escape(step) + '"}' for step in ex["how"])
    schema = '{{"@context":"https://schema.org","@type":"HowTo","name":"{}","description":"{}","totalTime":"PT{}S","tool":{{"@type":"HowToTool","name":"No equipment required"}},"step":[{}]}}'.format(
        h.escape(ex["name"]), h.escape(desc), ex["dose"], steps_json)

    video_schema = ""
    if ex["id"] in available_videos:
        video_schema = ',{{"@context":"https://schema.org","@type":"VideoObject","name":"{} — Exercise Guide","description":"{}","contentUrl":"https://baselinebody.app/assets/video/{}.mp4","thumbnailUrl":"https://baselinebody.app/assets/{}.png"}}'.format(
            h.escape(ex["name"]), h.escape(desc), ex["id"], ex["id"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h.escape(title)}</title>
<meta name="description" content="{h.escape(desc[:160])}">
<meta property="og:title" content="{h.escape(title)}">
<meta property="og:description" content="{h.escape(desc[:160])}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://baselinebody.app/exercises/{s}.html">
<link rel="canonical" href="https://baselinebody.app/exercises/{s}.html">
<link rel="icon" href="../assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/exercise.css">
<script type="application/ld+json">[{schema}{video_schema}]</script>
</head>
<body>

<header class="page-header">
  <a href="../index.html" class="logo"><div class="logo-mark"></div><span class="logo-text">BASELINE</span></a>
  <a href="../index.html#download" class="nav-cta">Download free</a>
</header>

<main class="container">
  <div class="breadcrumb"><a href="../index.html">Home</a><span>\u203a</span><a href="index.html">Exercises</a><span>\u203a</span>{h.escape(ex["name"])}</div>

  <div class="exercise-hero">
    <div class="category-badge" style="color:{color};background:{bg}">{cat_label} \u00b7 {ex["tier"]}</div>
    <h1>{h.escape(ex["name"])}</h1>
    <p class="tagline">{h.escape(ex["targets"])}</p>
  </div>

  <div class="dose-card">
    <div class="dose-label">Minimum Effective Dose</div>
    <div class="dose-time" style="color:{color}">{dose_fmt}</div>
    <div class="dose-explain">The shortest time that still creates real, measurable change. Hit the dose and the benefit starts. Everything after is bonus.</div>
  </div>
  {vid}
  <div class="content-section">
    <h2>Why it works</h2>
    <p>{h.escape(ex["why"])}</p>
  </div>

  <div class="content-section">
    <h2>How to do it</h2>
    <div class="cue-block">
      <div class="cue-title">{h.escape(ex["cue_title"])}</div>
      <div class="cue-detail">{h.escape(ex["cue_detail"])}</div>
    </div>
    <ul>{steps_html}</ul>
  </div>
  {variants_html}
  {related_html}
  <div class="cta-banner">
    <h3>Baseline builds this into your session automatically.</h3>
    <p>No choosing. No planning. The system decides what you need and tells you exactly what to do.</p>
    <a href="https://apps.apple.com/app/baseline/idYOUR_APP_ID" class="dl-btn">
      <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      Download free
    </a>
  </div>
</main>

<footer class="page-footer">
  <div class="footer-links">
    <a href="../index.html">Home</a>
    <a href="index.html">All Exercises</a>
    <a href="../disclaimer.html">Health Disclaimer</a>
    <a href="../privacy.html">Privacy Policy</a>
    <a href="mailto:support@baselinebody.app">Contact</a>
  </div>
  <p class="footer-copy">&copy; 2026 Baseline. Health without negotiation.</p>
</footer>

</body>
</html>'''


def shift_page(mode):
    s = mode["id"]
    title = f'{mode["title"]}: Breathwork for Shifting State | Baseline'
    desc = f'{mode["title"]} \u2014 {mode["state_from"]} \u2192 {mode["state_to"]}. {mode["breath_label"]}. Minimum effective dose: {format_dose(mode["dose"])}.'

    cues_html = ""
    if mode["physical_cues"]:
        items = "".join(f"<li>{h.escape(c)}</li>" for c in mode["physical_cues"])
        cues_html = f'''
    <div class="content-section">
      <h2>Physical cues</h2>
      <p style="color:var(--t3);font-size:14px;margin-bottom:12px">Body-addressed prompts that appear during the session:</p>
      <ul>{items}</ul>
    </div>'''

    attention_html = ""
    if mode["attention_lines"]:
        items = "".join(f"<li>{h.escape(l)}</li>" for l in mode["attention_lines"])
        attention_html = f'''
    <div class="content-section">
      <h2>Attention lines</h2>
      <ul>{items}</ul>
    </div>'''

    other_modes = [m for m in shift_modes if m["id"] != mode["id"]]
    related_cards = "".join(f'''<a class="related-card" href="{m["id"]}.html">
        <div class="related-name" style="color:{m["color_var"]}">{m["title"]}</div>
        <div class="related-dose">{m["state_from"]} \u2192 {m["state_to"]}</div>
      </a>''' for m in other_modes)

    schema = f'{{"@context":"https://schema.org","@type":"HowTo","name":"{h.escape(mode["title"])} Breathwork","description":"{h.escape(mode["description"])}","totalTime":"PT{mode["dose"]}S"}}'

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{h.escape(title)}</title>
<meta name="description" content="{h.escape(desc[:160])}">
<meta property="og:title" content="{h.escape(title)}">
<meta property="og:description" content="{h.escape(desc[:160])}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://baselinebody.app/shift/{s}.html">
<link rel="canonical" href="https://baselinebody.app/shift/{s}.html">
<link rel="icon" href="../assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/exercise.css">
<script type="application/ld+json">{schema}</script>
</head>
<body>

<header class="page-header">
  <a href="../index.html" class="logo"><div class="logo-mark"></div><span class="logo-text">BASELINE</span></a>
  <a href="../index.html#download" class="nav-cta">Download free</a>
</header>

<main class="container">
  <div class="breadcrumb"><a href="../index.html">Home</a><span>\u203a</span><a href="index.html">Shift</a><span>\u203a</span>{h.escape(mode["title"])}</div>

  <div class="exercise-hero">
    <div class="state-transition">FROM {h.escape(mode["state_from"].upper())} \u2192 {h.escape(mode["state_to"].upper())}</div>
    <h1 style="font-family:{mode["font_family"]};color:{mode["color_var"]}">{h.escape(mode["title"])}</h1>
    <p class="tagline">{h.escape(mode["description"])}</p>
  </div>

  <div class="dose-card">
    <div class="dose-label">Minimum Effective Dose</div>
    <div class="dose-time" style="color:{mode["color_var"]}">{format_dose(mode["dose"])}</div>
    <div class="dose-explain">Minimum session: {mode["min_duration"]}. Breath cycle: {mode["cycle"]} per round.</div>
  </div>

  <div class="content-section">
    <h2>Breath pattern</h2>
    <div class="breath-pattern">{mode["breath_html"]}</div>
    <p>{h.escape(mode["breath_label"])}</p>
  </div>

  <div class="content-section">
    <h2>When to use it</h2>
    <p>{h.escape(mode["example"])}</p>
  </div>

  <div class="content-section">
    <h2>The science</h2>
    <p>{h.escape(mode["science"])}</p>
  </div>
  {cues_html}
  {attention_html}
  <div class="content-section">
    <h2>Other Shift modes</h2>
    <div class="related-grid">{related_cards}</div>
  </div>

  <div class="cta-banner">
    <h3>Shift is built into Baseline.</h3>
    <p>The system picks the mode based on your state. Binaural beats, haptic feedback, and guided breathing \u2014 all automatic.</p>
    <a href="https://apps.apple.com/app/baseline/idYOUR_APP_ID" class="dl-btn">
      <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      Download free
    </a>
  </div>
</main>

<footer class="page-footer">
  <div class="footer-links">
    <a href="../index.html">Home</a>
    <a href="../exercises/index.html">All Exercises</a>
    <a href="index.html">All Shift Modes</a>
    <a href="../disclaimer.html">Health Disclaimer</a>
    <a href="../privacy.html">Privacy Policy</a>
    <a href="mailto:support@baselinebody.app">Contact</a>
  </div>
  <p class="footer-copy">&copy; 2026 Baseline. Health without negotiation.</p>
</footer>

</body>
</html>'''


def exercise_index():
    mobility = [e for e in exercises if e["category"] == "mobility"]
    bodyweight = [e for e in exercises if e["category"] == "bodyweight"]
    recovery = [e for e in exercises if e["category"] == "recovery"]

    def cards(exs, color):
        return "".join(f'''<a class="related-card" href="{slug(e["id"])}.html">
        <div class="related-name">{h.escape(e["name"])}</div>
        <div class="related-dose" style="color:{color}">Dose: {format_dose(e["dose"])}</div>
      </a>''' for e in exs)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exercise Library \u2014 Minimum Effective Dose for Every Movement | Baseline</title>
<meta name="description" content="Every exercise in Baseline, with its minimum effective dose. Mobility, bodyweight strength, and recovery \u2014 the shortest time that still creates real change.">
<link rel="canonical" href="https://baselinebody.app/exercises/">
<link rel="icon" href="../assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/exercise.css">
</head>
<body>
<header class="page-header">
  <a href="../index.html" class="logo"><div class="logo-mark"></div><span class="logo-text">BASELINE</span></a>
  <a href="../index.html#download" class="nav-cta">Download free</a>
</header>
<main class="container">
  <div class="breadcrumb"><a href="../index.html">Home</a><span>\u203a</span>Exercises</div>
  <div class="exercise-hero">
    <h1>Exercise Library</h1>
    <p class="tagline">Every exercise in Baseline, with its research-backed minimum effective dose. The shortest time that still creates real change.</p>
  </div>
  <div class="content-section">
    <h2 style="color:var(--green)">Mobility</h2>
    <p>Daily maintenance. Stretching, joint work, and decompression.</p>
    <div class="related-grid">{cards(mobility, "var(--green)")}</div>
  </div>
  <div class="content-section">
    <h2 style="color:var(--tangerine)">Bodyweight Strength</h2>
    <p>Push, pull, hold. No equipment. The system decides when you're ready to progress.</p>
    <div class="related-grid">{cards(bodyweight, "var(--tangerine)")}</div>
  </div>
  <div class="content-section">
    <h2 style="color:var(--steel)">Recovery</h2>
    <p>Nervous system regulation and active recovery.</p>
    <div class="related-grid">{cards(recovery, "var(--steel)")}</div>
  </div>
  <div class="content-section">
    <h2 style="color:var(--indigo)">Shift \u2014 Breathwork</h2>
    <p>Five breathwork protocols for shifting state. <a href="../shift/index.html">View all Shift modes \u2192</a></p>
  </div>
  <div class="cta-banner">
    <h3>You don't pick the exercises. The system does.</h3>
    <p>Baseline reads your body, builds your session, and tells you exactly what to do. Every day. Under 20 minutes.</p>
    <a href="https://apps.apple.com/app/baseline/idYOUR_APP_ID" class="dl-btn">
      <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      Download free
    </a>
  </div>
</main>
<footer class="page-footer">
  <div class="footer-links">
    <a href="../index.html">Home</a>
    <a href="../shift/index.html">Shift Modes</a>
    <a href="../disclaimer.html">Health Disclaimer</a>
    <a href="../privacy.html">Privacy Policy</a>
    <a href="mailto:support@baselinebody.app">Contact</a>
  </div>
  <p class="footer-copy">&copy; 2026 Baseline. Health without negotiation.</p>
</footer>
</body>
</html>'''


def shift_index():
    cards = "".join(f'''
    <a class="related-card" href="{m["id"]}.html" style="border-color:{m["color_hex"]}22">
      <div class="related-name" style="color:{m["color_var"]};font-family:{m["font_family"]}">{m["title"]}</div>
      <div class="related-dose">{m["state_from"]} \u2192 {m["state_to"]} \u00b7 Dose: {format_dose(m["dose"])}</div>
    </a>''' for m in shift_modes)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shift \u2014 Breathwork for Shifting State | Baseline</title>
<meta name="description" content="Five breathwork protocols for shifting your nervous system state. Arrive, Prime, Reset, Downshift, Override.">
<link rel="canonical" href="https://baselinebody.app/shift/">
<link rel="icon" href="../assets/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/exercise.css">
</head>
<body>
<header class="page-header">
  <a href="../index.html" class="logo"><div class="logo-mark"></div><span class="logo-text">BASELINE</span></a>
  <a href="../index.html#download" class="nav-cta">Download free</a>
</header>
<main class="container">
  <div class="breadcrumb"><a href="../index.html">Home</a><span>\u203a</span>Shift</div>
  <div class="exercise-hero">
    <h1>Shift</h1>
    <p class="tagline">Five breathwork protocols for shifting your nervous system state. Each mode targets a specific autonomic transition.</p>
  </div>
  <div class="content-section">
    <h2>Choose your state</h2>
    <div class="related-grid" style="grid-template-columns:1fr">{cards}</div>
  </div>
  <div class="cta-banner">
    <h3>You don't choose. The system reads your state.</h3>
    <p>Binaural beats, haptic feedback, and guided breathing. All automatic. Built into Baseline.</p>
    <a href="https://apps.apple.com/app/baseline/idYOUR_APP_ID" class="dl-btn">
      <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.8-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>
      Download free
    </a>
  </div>
</main>
<footer class="page-footer">
  <div class="footer-links">
    <a href="../index.html">Home</a>
    <a href="../exercises/index.html">All Exercises</a>
    <a href="../disclaimer.html">Health Disclaimer</a>
    <a href="../privacy.html">Privacy Policy</a>
    <a href="mailto:support@baselinebody.app">Contact</a>
  </div>
  <p class="footer-copy">&copy; 2026 Baseline. Health without negotiation.</p>
</footer>
</body>
</html>'''


# ─────────────────────────────────────────────
# GENERATE
# ─────────────────────────────────────────────

if __name__ == "__main__":
    ex_dir = os.path.join(BASE, "exercises")
    sh_dir = os.path.join(BASE, "shift")
    count = 0
    videos_used = 0

    for ex in exercises:
        path = os.path.join(ex_dir, f"{slug(ex['id'])}.html")
        with open(path, "w") as f:
            f.write(exercise_page(ex))
        if ex["id"] in available_videos:
            videos_used += 1
        count += 1

    with open(os.path.join(ex_dir, "index.html"), "w") as f:
        f.write(exercise_index())
    count += 1

    for mode in shift_modes:
        path = os.path.join(sh_dir, f"{mode['id']}.html")
        with open(path, "w") as f:
            f.write(shift_page(mode))
        count += 1

    with open(os.path.join(sh_dir, "index.html"), "w") as f:
        f.write(shift_index())
    count += 1

    print(f"Generated {count} pages ({videos_used} with video)")
    print(f"Videos available: {len(available_videos)}")
    print(f"Exercises in catalog: {len(exercises)}")
