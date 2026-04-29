---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_identity_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-identity-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_identity_check",
  "declaration_slug": "preyoneda-identity-check",
  "kind": "def",
  "name": "preyoneda_identity_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 100,
  "source_line_end": 110,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L100-L110",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L100-L110",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L100-L110)
- Source range: L100-L110
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pre-Yoneda preserves the identity: preyoneda(id, x, k) = reduce(x, k).
    The identity function embeds as the canonical reduction map. -/
```

## Source Excerpt

```lean
def preyoneda_identity_check (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let embed := preyoneda_embed_nat (fun n => n) x k
      (embed == reduce x k) && go x (k + 1) (fuel - 1)
  termination_by fuel
```
