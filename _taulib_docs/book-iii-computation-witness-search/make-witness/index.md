---
{
  "projection_kind": "taulib_declaration",
  "title": "make_witness",
  "permalink": "/verify/taulib/docs/book-iii-computation-witness-search/make-witness/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Computation.WitnessSearch`.",
  "declaration_id": "TauLib.BookIII.Computation.WitnessSearch::make_witness",
  "declaration_slug": "make-witness",
  "kind": "def",
  "name": "make_witness",
  "module_name": "TauLib.BookIII.Computation.WitnessSearch",
  "module_url": "/verify/taulib/docs/book-iii-computation-witness-search/",
  "source_line_start": 51,
  "source_line_end": 56,
  "registry_ids": [
    "III.D55"
  ],
  "related_registry_items": [
    {
      "id": "III.D55",
      "title": "NP Witness as Canonical Address",
      "url": "/registry/object/III.D55/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L51-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.WitnessSearch",
        "url": "/verify/taulib/docs/book-iii-computation-witness-search/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L51-L56",
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

- Module: [TauLib.BookIII.Computation.WitnessSearch](/verify/taulib/docs/book-iii-computation-witness-search/)
- Source path: [`TauLib/BookIII/Computation/WitnessSearch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/WitnessSearch.lean#L51-L56)
- Source range: L51-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D55` — NP Witness as Canonical Address

## Immediate Comment / Docstring

```lean
/-- [III.D55] Construct a witness from a value and depth. -/
```

## Source Excerpt

```lean
def make_witness (x k : TauIdx) : WitnessAddress :=
  let pk := primorial k
  if pk == 0 then ⟨0, k, 0, 0, 0⟩
  else
    let nf := boundary_normal_form (x % pk) k
    ⟨x % pk, k, nf.b_part, nf.c_part, nf.x_part⟩
```
