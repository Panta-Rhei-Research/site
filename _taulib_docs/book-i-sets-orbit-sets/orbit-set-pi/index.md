---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_pi",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-pi/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_pi",
  "declaration_slug": "orbit-set-pi",
  "kind": "def",
  "name": "orbit_set_pi",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 87,
  "source_line_end": 91,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L87-L91",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L87-L91",
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
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L87-L91)
- Source range: L87-L91
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D94` — Orbit-Set Map

## Immediate Comment / Docstring

```lean
/-- [I.D94] Set(π_n): the set of α-orbit indices belonging to the
    orbit-set of π_n.
    α_k ∈ Set(π_n) iff k = 1 or there exists j ≤ n with k = nthPrime j. -/
```

## Source Excerpt

```lean
def orbit_set_pi (n : TauIdx) (k : TauIdx) : Prop :=
  k = 1 ∨ ∃ j, j ≤ n ∧ k = nthPrime j

noncomputable instance instDecidableOrbitSetPi (n k : TauIdx) :
    Decidable (orbit_set_pi n k) := Classical.dec _
```
