---
{
  "projection_kind": "taulib_declaration",
  "title": "sigma",
  "permalink": "/corpus/taulib/docs/book-i-denotation-tau-idx/sigma/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.TauIdx`.",
  "declaration_id": "TauLib.BookI.Denotation.TauIdx::sigma",
  "declaration_slug": "sigma",
  "kind": "def",
  "name": "sigma",
  "module_name": "TauLib.BookI.Denotation.TauIdx",
  "module_url": "/corpus/taulib/docs/book-i-denotation-tau-idx/",
  "source_line_start": 80,
  "source_line_end": 83,
  "registry_ids": [
    "I.D09"
  ],
  "related_registry_items": [
    {
      "id": "I.D09",
      "title": "Swap Operator sigma",
      "url": "/registry/object/I.D09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L80-L83",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L80-L83",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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
- Source path: [`TauLib/BookI/Denotation/TauIdx.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/TauIdx.lean#L80-L83)
- Source range: L80-L83
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `I.D09` — Swap Operator sigma

## Immediate Comment / Docstring

```lean
/-- [I.D09] The swap operator σ_{s,t}: exchanges seeds s and t,
    leaving all other seeds unchanged. Preserves depth. -/
```

## Source Excerpt

```lean
def sigma (s t : Generator) (x : TauObj) : TauObj :=
  if x.seed = s then ⟨t, x.depth⟩
  else if x.seed = t then ⟨s, x.depth⟩
  else x
```
