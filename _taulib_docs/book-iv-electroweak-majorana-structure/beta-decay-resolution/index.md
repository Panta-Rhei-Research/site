---
{
  "projection_kind": "taulib_declaration",
  "title": "beta_decay_resolution",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/beta-decay-resolution/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.MajoranaStructure`.",
  "declaration_id": "TauLib.BookIV.Electroweak.MajoranaStructure::beta_decay_resolution",
  "declaration_slug": "beta-decay-resolution",
  "kind": "def",
  "name": "beta_decay_resolution",
  "module_name": "TauLib.BookIV.Electroweak.MajoranaStructure",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/",
  "source_line_start": 174,
  "source_line_end": 178,
  "registry_ids": [
    "IV.P186"
  ],
  "related_registry_items": [
    {
      "id": "IV.P186",
      "title": "beta-Decay nu/nu-bar as Helicity Labels (not particle/antiparticle)",
      "url": "/registry/object/IV.P186/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L174-L178",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.MajoranaStructure",
        "url": "/verify/taulib/docs/book-iv-electroweak-majorana-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L174-L178",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIV.Electroweak.MajoranaStructure](/verify/taulib/docs/book-iv-electroweak-majorana-structure/)
- Source path: [`TauLib/BookIV/Electroweak/MajoranaStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/MajoranaStructure.lean#L174-L178)
- Source range: L174-L178
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P186` — beta-Decay nu/nu-bar as Helicity Labels (not particle/antiparticle)

## Immediate Comment / Docstring

```lean
/-- [IV.P186] In β⁻ decay (n → p + e⁻ + "ν̄_e"), the "ν̄_e" label denotes
    the Majorana neutrino emitted with right-handed helicity (past-directed τ¹).
    In β⁺ decay (p → n + e⁺ + "ν_e"), the "ν_e" is the same particle with
    left-handed helicity (future-directed τ¹).

    The distinction ν vs ν̄ is a kinematic label (helicity), NOT an internal
    quantum number. Lepton number L is not conserved in Category τ. -/
```

## Source Excerpt

```lean
def beta_decay_resolution : String :=
  "In beta^- decay: nu_bar_e = right-handed Majorana neutrino (past-directed tau^1). " ++
  "In beta^+ decay: nu_e = left-handed Majorana neutrino (future-directed tau^1). " ++
  "Same Majorana particle, different helicity. Lepton number L not conserved in tau. " ++
  "The overbar is a helicity label, not a particle/antiparticle distinction."
```
