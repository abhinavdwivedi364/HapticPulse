# ⚡ HapticPulse

> **The Tactile Anchor for Neurodivergent Deep Work.**

`HapticPulse` is a minimalist productivity tool designed for individuals with ADHD and executive dysfunction.

Since not everyone has access to specialized devices or watches that bring this functionality, I experimented with other means to achieve this. This solution leverages the haptic hardware of a PlayStation 4 (DualShock 4) controller to provide non-intrusive "Focus Check-ins" through vibration. My reasoning was that probably many people have some sort of Gamecontroller at home lying around.

This allows you to plugin the controller put it next to you on your desk while working and run this program.

---

## 🧠 The Science: Why Haptic Feedback?

For the neurodivergent brain, traditional productivity tools often fail due to specific neurological challenges:

### 1. Time Blindness (Dyschronometria)

People with ADHD often experience "Time Blindness"—a difficulty in perceiving the passage of time. According to **Dr. Russell Barkley**, a leading expert on ADHD, the disorder is fundamentally a "disorder of self-regulation and time." Externalizing time is crucial for maintaining focus.

- **The Haptic Solution:** Instead of relying on internal perception, `HapticPulse` externalizes time into a physical sensation, creating a "tactile anchor" in the real world.

### 2. The Auditory Startle Response vs. Flow

Sudden auditory alarms can be jarring, triggering a startle response that shatters the state of **Hyperfocus** or **Flow**.

- **The Haptic Solution:** Research into **Somatosensory Cues** suggests that tactile stimulation is processed differently than auditory or visual input. A vibration provides a "gentle nudge" that allows for a cognitive check-in without breaking the current mental loop.

### 🔬 Research & References

- **Barkley, R. A. (1997):** _ADHD and the Nature of Self-Control._ (Focus on the necessity of externalizing time).
- **Haptic Prompts:** Studies on wearable technology have shown that automated haptic reminders can significantly increase "on-task behavior" in individuals with ADHD. [See related research on NCBI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6400613/).

---

## ✨ Features

- **Zero-UI Design:** No windows, no tabs, no visual clutter to distract you.
- **PS4/DualShock 4 Integration:** Professional-grade haptic motors for nuanced feedback.
- **Modern CLI:** Built with `Typer` and `Rich` for a beautiful developer experience.
- **Test Mode:** Built-in hardware diagnostics to ensure your connection is solid.

---

## 🛠 Installation

1. **Clone the repository & install:**

   ```bash
   git clone https://github.com/your-username/HapticPulse.git
   cd HapticPulse
   pip install -e .
   ```

2. **Connect the Controller via USB + run the test command (Controller should vibrate):**

   ```bash
    haptic-pulse test
   ```

3. **Run the command + configure to your liking:**
   ```bash
    python -m haptic_pulse --interval 45 --strength 0.5
   ```
   <b>Strength</b> 0.1-1</br>
   <b>Interval</b> How long a focus session should be in min
