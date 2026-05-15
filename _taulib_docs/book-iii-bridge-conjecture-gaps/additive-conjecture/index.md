---
{
  "projection_kind": "taulib_declaration",
  "title": "AdditiveConjecture",
  "permalink": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/additive-conjecture/",
  "summary_short": "`inductive` declaration in `TauLib.BookIII.Bridge.ConjectureGaps`.",
  "declaration_id": "TauLib.BookIII.Bridge.ConjectureGaps::AdditiveConjecture",
  "declaration_slug": "additive-conjecture",
  "kind": "inductive",
  "name": "AdditiveConjecture",
  "module_name": "TauLib.BookIII.Bridge.ConjectureGaps",
  "module_url": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/",
  "source_line_start": 108,
  "source_line_end": 112,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L108-L112",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ConjectureGaps",
        "url": "/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L108-L112",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "inductive",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIII.Bridge.ConjectureGaps](/corpus/taulib/docs/book-iii-bridge-conjecture-gaps/)
- Source path: [`TauLib/BookIII/Bridge/ConjectureGaps.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ConjectureGaps.lean#L108-L112)
- Source range: L108-L112
- Kind: `inductive`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Classification of the three conjectures. -/
```

## Source Excerpt

```lean
inductive AdditiveConjecture where
  | goldbach    -- every even n ≥ 4 is the sum of two primes
  | twin_primes -- infinitely many pairs (p, p+2)
  | abc         -- for coprime a+b=c: c < rad(abc)^{1+ε}
  deriving Repr, DecidableEq, BEq
```
