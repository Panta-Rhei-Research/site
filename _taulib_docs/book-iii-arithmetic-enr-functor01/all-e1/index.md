---
{
  "projection_kind": "taulib_declaration",
  "title": "all_e1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/all-e1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.EnrFunctor01`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.EnrFunctor01::all_e1",
  "declaration_slug": "all-e1",
  "kind": "theorem",
  "name": "all_e1",
  "module_name": "TauLib.BookIII.Arithmetic.EnrFunctor01",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/",
  "source_line_start": 160,
  "source_line_end": 165,
  "registry_ids": [
    "III.P24"
  ],
  "related_registry_items": [
    {
      "id": "III.P24",
      "title": "Three-Reading Equivalence at E₁",
      "url": "/registry/object/III.P24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L160-L165",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.EnrFunctor01",
        "url": "/verify/taulib/docs/book-iii-arithmetic-enr-functor01/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L160-L165",
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

- Module: [TauLib.BookIII.Arithmetic.EnrFunctor01](/verify/taulib/docs/book-iii-arithmetic-enr-functor01/)
- Source path: [`TauLib/BookIII/Arithmetic/EnrFunctor01.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/EnrFunctor01.lean#L160-L165)
- Source range: L160-L165
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P24` — Three-Reading Equivalence at E₁

## Immediate Comment / Docstring

```lean
/-- [III.P24] Structural: NS, YM, Hodge are all at E₁. -/
```

## Source Excerpt

```lean
theorem all_e1 :
    (problem_level .NS == .E1 &&
    problem_level .YM == .E1 &&
    problem_level .Hodge == .E1) = true := by native_decide

end Tau.BookIII.Arithmetic
```
