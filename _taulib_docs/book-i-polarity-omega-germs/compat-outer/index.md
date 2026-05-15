---
{
  "projection_kind": "taulib_declaration",
  "title": "compat_outer",
  "permalink": "/corpus/taulib/docs/book-i-polarity-omega-germs/compat-outer/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::compat_outer",
  "declaration_slug": "compat-outer",
  "kind": "def",
  "name": "compat_outer",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/corpus/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 85,
  "source_line_end": 89,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L85-L89",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L85-L89",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/corpus/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L85-L89)
- Source range: L85-L89
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Check full compatibility of an omega-tail.
    Wave 38: stage indices `d`, `k` are now `TauIdx`. -/
```

## Source Excerpt

```lean
def compat_outer (comps : List TauIdx) (d k : TauIdx) (fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if k > d then true
  else compat_inner comps k d d && compat_outer comps d (k + 1) (fuel - 1)
termination_by fuel
```
