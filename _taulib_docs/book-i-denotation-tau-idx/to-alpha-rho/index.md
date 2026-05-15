---
{
  "projection_kind": "taulib_declaration",
  "title": "toAlpha_rho",
  "permalink": "/corpus/taulib/docs/book-i-denotation-tau-idx/to-alpha-rho/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.TauIdx`.",
  "declaration_id": "TauLib.BookI.Denotation.TauIdx::toAlpha_rho",
  "declaration_slug": "to-alpha-rho",
  "kind": "theorem",
  "name": "toAlpha_rho",
  "module_name": "TauLib.BookI.Denotation.TauIdx",
  "module_url": "/corpus/taulib/docs/book-i-denotation-tau-idx/",
  "source_line_start": 70,
  "source_line_end": 72,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L70-L72",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.TauIdx",
        "url": "/corpus/taulib/docs/book-i-denotation-tau-idx/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L70-L72",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Denotation.TauIdx](/corpus/taulib/docs/book-i-denotation-tau-idx/)
- Source path: [`TauLib/BookI/Denotation/TauIdx.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L70-L72)
- Source range: L70-L72
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The embedding commutes with ρ: toAlpha(n+1) = ρ(toAlpha(n)). -/
```

## Source Excerpt

```lean
theorem toAlpha_rho (n : TauIdx) :
    toAlphaOrbit (n + 1) = rho (toAlphaOrbit n) := by
  simp [toAlphaOrbit, rho]
```
