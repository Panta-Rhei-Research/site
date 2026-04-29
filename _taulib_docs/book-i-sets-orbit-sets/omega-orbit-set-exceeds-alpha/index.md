---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_orbit_set_exceeds_alpha",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/omega-orbit-set-exceeds-alpha/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::omega_orbit_set_exceeds_alpha",
  "declaration_slug": "omega-orbit-set-exceeds-alpha",
  "kind": "theorem",
  "name": "omega_orbit_set_exceeds_alpha",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 220,
  "source_line_end": 222,
  "registry_ids": [
    "I.R28"
  ],
  "related_registry_items": [
    {
      "id": "I.R28",
      "title": "Inseparability of N and omega",
      "url": "/registry/object/I.R28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L220-L222",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.OrbitSets",
        "url": "/verify/taulib/docs/book-i-sets-orbit-sets/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L220-L222",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L220-L222)
- Source range: L220-L222
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.R28` — Inseparability of N and omega

## Immediate Comment / Docstring

```lean
/-- [I.R28] ω's orbit-set includes ω itself, so it does not live purely
    in the α-orbit. This is the TauObj-level witness that Set(ω) ≠ O_α. -/
```

## Source Excerpt

```lean
theorem omega_orbit_set_exceeds_alpha :
    orbit_set_omega ⟨omega, 0⟩ ∧ (⟨omega, 0⟩ : TauObj).seed ≠ alpha :=
  ⟨self_containment_omega, by simp⟩
```
