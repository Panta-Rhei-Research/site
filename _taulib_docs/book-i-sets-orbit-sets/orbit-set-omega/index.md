---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_omega",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-omega/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_omega",
  "declaration_slug": "orbit-set-omega",
  "kind": "def",
  "name": "orbit_set_omega",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 130,
  "source_line_end": 135,
  "registry_ids": [
    "I.D94"
  ],
  "related_registry_items": [
    {
      "id": "I.D94",
      "title": "Orbit-Set Map",
      "url": "/registry/object/I.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L130-L135",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L130-L135",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L130-L135)
- Source range: L130-L135
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D94` — Orbit-Set Map

## Immediate Comment / Docstring

```lean
/-- [I.D94] Set(ω): the set of τ-objects belonging to the orbit-set of ω.
    x ∈ Set(ω) iff x.seed = alpha or (x.seed = omega and x.depth = 0).

    Note: this predicate acts on TauObj, not TauIdx — ω's orbit-set
    includes itself (the TauObj ⟨omega, 0⟩), which cannot be represented
    as a pure TauIdx predicate. Set(ω) = O_α ∪ {ω} is the universal
    collection — one-point compactification of the counting scaffold. -/
```

## Source Excerpt

```lean
def orbit_set_omega (x : TauObj) : Prop :=
  x.seed = alpha ∨ (x.seed = omega ∧ x.depth = 0)

instance instDecidableOrbitSetOmega (x : TauObj) :
    Decidable (orbit_set_omega x) := by
  unfold orbit_set_omega; exact instDecidableOr
```
