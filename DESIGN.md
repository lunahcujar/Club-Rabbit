---
name: Elite Athleticism
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#e9c400'
  on-tertiary: '#3a3000'
  tertiary-container: '#c9a900'
  on-tertiary-container: '#4c3f00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

This design system embodies the high-energy, premium nature of a competitive volleyball club. The brand personality is **authoritative, energetic, and prestigious**, targeting athletes and fans who value performance and community. 

The visual style is a fusion of **Corporate Modern** and **High-Contrast Bold**. It utilizes deep, cinematic backgrounds to make gold and vibrant orange accents pop, mimicking the atmosphere of a professional arena under spotlights. The interface relies on clean lines, intentional use of motion, and premium finishing touches like metallic gradients and subtle light leaks to evoke a sense of victory and elite status.

## Colors

The palette is anchored by **Deep Navy Blue**, providing a sophisticated and stable foundation. **Metallic Gold** is used for prestige elements, borders, and primary branding. **Vibrant Orange/Yellow** serves as a high-visibility action color for call-to-actions and critical data points, drawing direct inspiration from the kinetic energy of a volleyball in play.

- **Primary:** Use for large background areas and core branding.
- **Secondary (Gold):** Reserved for decorative borders, iconography, and luxury accents.
- **Tertiary (Accent):** Specifically for interactive states and urgent information.
- **Neutral:** Pure white is used exclusively for high-readability body text and "reversed" UI elements.

## Typography

The typography system strikes a balance between **athletic power** and **digital clarity**. 

- **Headlines:** Montserrat is utilized in heavy weights (Bold/ExtraBold) to convey strength. For the most prominent titles, use `display-lg` with tight letter spacing to mimic sports jersey aesthetics.
- **Body:** Be Vietnam Pro (a modern alternative to Poppins with better technical legibility) is used for all long-form content. It maintains a friendly yet professional tone.
- **Labels:** Small labels and navigational items use uppercase Montserrat to maintain the "club" identity even at small scales.

## Layout & Spacing

The design system employs a **12-column fluid grid** for desktop and a **4-column grid** for mobile. 

- **Rhythm:** An 8px base unit drives all spatial decisions. 
- **Density:** The layout is "Airy yet Structured." Use `lg` and `xl` spacing for section breaks to allow the photography and high-contrast elements room to breathe.
- **Safe Areas:** On mobile, maintain a minimum `margin-mobile` of 16px. On desktop, content should be capped at a max-width of 1280px to ensure line lengths remain readable.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Subtle Glows**. 

1. **Surface 0 (Background):** Deepest Navy (#000D1A).
2. **Surface 1 (Cards):** Slightly lighter Navy (#00162E) with a 1px Gold border at 30% opacity.
3. **Elevated State:** Elements "lift" using a subtle 15% opacity Gold outer glow rather than a traditional black shadow. 

This creates a "lit from within" effect that feels more like a stadium scoreboard or premium trophy case than a standard website.

## Shapes

The shape language is defined by **Controlled Curvature**. 

A standard `rounded-md` (0.5rem) is used for most UI containers to keep them feeling modern and approachable. However, for interactive elements like Buttons and Chips, use "Pill" styling (fully rounded) to mirror the spherical nature of the volleyball and provide a friendly, high-performance feel.

## Components

### Buttons
- **Primary:** Vibrant Orange background, White bold text. On hover, transition to a Metallic Gold gradient with a subtle 4px scale increase.
- **Secondary:** Transparent with a 2px Gold border. Text is Gold. Hover state fills the button with Gold and changes text to Navy.

### Cards
- **Structure:** Surface 1 background, rounded-lg (1rem). 
- **Detail:** Every card must feature a 1px top-border in Gold (#D4AF37) to lead the eye. 
- **Shadow:** Use a soft, deep navy shadow (0 8px 32px rgba(0,0,0,0.4)).

### Input Fields
- Dark Navy background, 1px White border (20% opacity).
- Active state: Border becomes 1px Solid Gold with a subtle gold inner-glow.

### Chips & Badges
- Used for "Categories" and "Status". Small, uppercase Montserrat text inside a pill-shaped container.
- Use the Vibrant Orange accent for active/live statuses.

### Lists
- Items separated by 1px Navy-Light lines. Use Gold icons for bullet points or leading indicators to reinforce the premium brand.