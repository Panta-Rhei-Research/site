---
{
  "projection_kind": "taulib_declaration",
  "title": "EMCouplingRelation",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewmixing/emcoupling-relation/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.EWMixing`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWMixing::EMCouplingRelation",
  "declaration_slug": "emcoupling-relation",
  "kind": "structure",
  "name": "EMCouplingRelation",
  "module_name": "TauLib.BookIV.Electroweak.EWMixing",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/",
  "source_line_start": 340,
  "source_line_end": 351,
  "registry_ids": [
    "IV.P68"
  ],
  "related_registry_items": [
    {
      "id": "IV.P68",
      "title": "Coupling Relations",
      "url": "/registry/object/IV.P68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L340-L351",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWMixing",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewmixing/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L340-L351",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookIV.Electroweak.EWMixing](/verify/taulib/docs/book-iv-electroweak-ewmixing/)
- Source path: [`TauLib/BookIV/Electroweak/EWMixing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWMixing.lean#L340-L351)
- Source range: L340-L351
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.P68` — Coupling Relations

## Immediate Comment / Docstring

```lean
/-- [IV.P68] The electromagnetic coupling e is related to the weak
    coupling g by e = g · sin(θ_W).
    In the τ-framework, this structural relationship means the EM
    coupling factors through the weak sector via the Weinberg angle.
    The EM self-coupling κ(B;2) = ι_τ² relates to κ(A;1) = ι_τ and
    the electroweak cross-coupling κ(A,B) = ι_τ²(1−ι_τ). -/
```

## Source Excerpt

```lean
structure EMCouplingRelation where
  /-- EM self-coupling sector. -/
  em : Sector := .B
  /-- Weak self-coupling sector. -/
  weak : Sector := .A
  /-- Mixing parameter sector pair. -/
  mixing_pair_i : Sector := .A
  mixing_pair_j : Sector := .D
  /-- All sectors assigned correctly. -/
  em_is_B : em = .B := by rfl
  weak_is_A : weak = .A := by rfl
  deriving Repr
```
