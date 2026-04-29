---
{
  "projection_kind": "taulib_declaration",
  "title": "presheaf_assign",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/presheaf-assign/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::presheaf_assign",
  "declaration_slug": "presheaf-assign",
  "kind": "def",
  "name": "presheaf_assign",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 58,
  "source_line_end": 59,
  "registry_ids": [
    "II.D47"
  ],
  "related_registry_items": [
    {
      "id": "II.D47",
      "title": "Holomorphic Presheaf",
      "url": "/registry/object/II.D47/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L58-L59",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L58-L59",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L58-L59)
- Source range: L58-L59
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D47` — Holomorphic Presheaf

## Immediate Comment / Docstring

```lean
/-- [II.D47] Cylinder membership predicate:
    presheaf_assign(k, a, x) is true iff x belongs to cylinder C_{k,a},
    i.e., reduce(x, k) == a.

    The cylinder C_{k,a} consists of all x ∈ Z/P_kZ with x mod P_k == a.
    In the full primorial tower, it consists of all x with reduce(x,k) == a. -/
```

## Source Excerpt

```lean
def presheaf_assign (k a x : TauIdx) : Bool :=
  reduce x k == a
```
