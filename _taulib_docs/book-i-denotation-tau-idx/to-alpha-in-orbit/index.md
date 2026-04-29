---
{
  "projection_kind": "taulib_declaration",
  "title": "toAlpha_in_orbit",
  "permalink": "/verify/taulib/docs/book-i-denotation-tau-idx/to-alpha-in-orbit/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.TauIdx`.",
  "declaration_id": "TauLib.BookI.Denotation.TauIdx::toAlpha_in_orbit",
  "declaration_slug": "to-alpha-in-orbit",
  "kind": "theorem",
  "name": "toAlpha_in_orbit",
  "module_name": "TauLib.BookI.Denotation.TauIdx",
  "module_url": "/verify/taulib/docs/book-i-denotation-tau-idx/",
  "source_line_start": 65,
  "source_line_end": 67,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L65-L67",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.TauIdx",
        "url": "/verify/taulib/docs/book-i-denotation-tau-idx/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L65-L67",
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

- Module: [TauLib.BookI.Denotation.TauIdx](/verify/taulib/docs/book-i-denotation-tau-idx/)
- Source path: [`TauLib/BookI/Denotation/TauIdx.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L65-L67)
- Source range: L65-L67
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The embedding lands in the alpha orbit ray. -/
```

## Source Excerpt

```lean
theorem toAlpha_in_orbit (n : TauIdx) :
    OrbitRay alpha (toAlphaOrbit n) := by
  exact ⟨rfl, by decide⟩
```
