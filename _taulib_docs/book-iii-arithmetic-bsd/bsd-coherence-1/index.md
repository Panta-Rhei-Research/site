---
{
  "projection_kind": "taulib_declaration",
  "title": "bsd_coherence_1",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-bsd/bsd-coherence-1/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.BSD`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.BSD::bsd_coherence_1",
  "declaration_slug": "bsd-coherence-1",
  "kind": "theorem",
  "name": "bsd_coherence_1",
  "module_name": "TauLib.BookIII.Arithmetic.BSD",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-bsd/",
  "source_line_start": 145,
  "source_line_end": 146,
  "registry_ids": [
    "III.T35"
  ],
  "related_registry_items": [
    {
      "id": "III.T35",
      "title": "BSD Coherence Theorem",
      "url": "/registry/object/III.T35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L145-L146",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.BSD",
        "url": "/verify/taulib/docs/book-iii-arithmetic-bsd/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L145-L146",
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

- Module: [TauLib.BookIII.Arithmetic.BSD](/verify/taulib/docs/book-iii-arithmetic-bsd/)
- Source path: [`TauLib/BookIII/Arithmetic/BSD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/BSD.lean#L145-L146)
- Source range: L145-L146
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T35` — BSD Coherence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T35] Structural: BSD coherence at depth 1. -/
```

## Source Excerpt

```lean
theorem bsd_coherence_1 :
    bsd_coherence_check 1 = true := by native_decide
```
