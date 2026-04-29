---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_gamma",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-gamma/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_gamma",
  "declaration_slug": "orbit-set-gamma",
  "kind": "def",
  "name": "orbit_set_gamma",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 100,
  "source_line_end": 104,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L100-L104",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L100-L104",
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
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L100-L104)
- Source range: L100-L104
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D94` — Orbit-Set Map

## Immediate Comment / Docstring

```lean
/-- [I.D94] Set(γ_n): the set of α-orbit indices belonging to the
    orbit-set of γ_n.
    α_k ∈ Set(γ_n) iff k = p_n ^ e for some e ≥ 0, where p_n = nthPrime n. -/
```

## Source Excerpt

```lean
def orbit_set_gamma (n : TauIdx) (k : TauIdx) : Prop :=
  ∃ e : TauIdx, k = (nthPrime n) ^ e

noncomputable instance instDecidableOrbitSetGamma (n k : TauIdx) :
    Decidable (orbit_set_gamma n k) := Classical.dec _
```
